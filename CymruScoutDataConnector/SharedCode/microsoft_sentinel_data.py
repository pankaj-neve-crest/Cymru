import json
import requests
import traceback
from datetime import datetime, timezone
import hashlib
import hmac
import base64
from ..SharedCode import constants
from .logger import apploger

class MicrosoftSentinel:
    def __init__(self) -> None:
        pass
    

    def build_signature(self, date, content_length, method, content_type, resource):
        x_headers = "x-ms-date:" + date
        string_to_hash = (
                method
                + "\n"
                + str(content_length)
                + "\n"
                + content_type
                + "\n"
                + x_headers
                + "\n"
                + resource
        )
        bytes_to_hash = bytes(string_to_hash, encoding="utf-8")  
        decoded_key = base64.b64decode(constants.WorkspaceKey)
        encoded_hash =  base64.b64encode(
            hmac.new(decoded_key, bytes_to_hash, 
                    digestmod=hashlib.sha256).digest()
        ).decode()
        authorization = "SharedKey {}:{}".format(constants.WorkspaceID,
                                                encoded_hash)
        return authorization
    

    def post_data(self, body, log_type):
        method = "POST"
        content_type = "application/json"
        resource = "/api/logs"
        # rfc1123date = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
        rfc1123date = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
        apploger.info("Date Formate is: {}".format(rfc1123date))
        content_length = len(body)
        try:
            signature = self.build_signature(rfc1123date, content_length,
                                             method, content_type, resource)
        except Exception as e:
            apploger.error("Error occurred: {}".format(e))
            raise Exception(
                "Error while generating signature for posting data into log analytics."
            )
        uri = (constants.LogAnaltyicsUri.format(constants.WorkspaceID, resource))
        # uri = ("https://" + constants.WORKSPACE_ID + ".ods.opinsights.azure.com" + resource + "?api-version=2016-04-01")
        headers = {
            "content-type": content_type,
            "Authorization": signature,
            "Log-Type": log_type,
            "x-ms-date": rfc1123date,
        }
        apploger.debug("headers : {}".format(headers))
        apploger.debug("POST BODY : {}".format(body))
        apploger.debug("BODY TYPE : {}".format(type(body)))
        try:
            response = requests.post(uri, data=body, headers=headers)
            if response.status_code < 200 or response.status_code > 299:
                raise Exception(
                    "Response code: {} from posting data to log analytics.\n Error: {}".format(
                        response.status_code, response.content
                    )
                )
            apploger.debug("DONE")
        except Exception as e:
            apploger.error(e)
            raise Exception("Exception: Error while posting data to sentinel.")
        
        return response.status_code   
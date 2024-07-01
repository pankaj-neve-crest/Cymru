import traceback
import json
import logging
from ..SharedCode.logger import apploger
import requests
from ..SharedCode import constants
from ..SharedCode.microsoft_sentinel_data import MicrosoftSentinel

class ScoutToAzureStorage(object):
    def __init__(self, start_time) -> None:
        self.start_time = start_time


    def get_request(self, url, headers, payload):
        apploger.debug("Calling API request")
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code == 200:
            apploger.info("Get response from API: "
                         "status code: {}".format(response.status_code))
            return response
        elif response.status_code == 500:
            raise Exception("Internal Error -There was an internal server "
                            "error:status code: {}".format(response.status_code))
        elif response.status_code == 429:
            raise Exception("Maximum concurrent requests have been exceeded: "
                            "status code: {}".format(response.status_code))
        elif response.status_code == 403:
            raise Exception("Authorization Error: You are not authorized to view this resource: "
                            "status code: {}".format(response.status_code))
        elif response.status_code == 401:
            raise Exception("Authentication Error: authorization token.: "
                            "status code: {}".format(response.status_code))
        elif response.status_code == 400:
            raise Exception("Bad Request: The request was malformed.: "
                            "status code: {}".format(response.status_code))


    def generate_request(self, ip):
        """
        Generate the API request and return response
        @rtype: object
        @param ip:
        @return:
        """
        apploger.info("Get IP details from API")
        url = constants.ScouCymrutBaseURL + constants.ScoutCymruIPSectionsDetailsURL.format(ip)
        headers = {'Authorization': constants.ScoutCymruAPIToken}
        payload = {}
        response = self.get_request(url, headers, payload)

        return response


    def get_scout_ip_data(self, ip) -> None:
        try:
            apploger.info("Get IP details from API")
            response = self.generate_request(ip)
            data = response.json()
            apploger.info("Response apploger")
            ms_sentinel_obj = MicrosoftSentinel()
            output = ms_sentinel_obj.post_data(
                json.dumps(data), constants.IP_PDNS_TABLE_NAME
            )
            apploger.info("Sentinel post data response: {}".format(output))
        except Exception as e:
            apploger.error("Error occured while fetch data, {}".format(e))
            apploger.error(traceback.format_exc())
            raise(e)

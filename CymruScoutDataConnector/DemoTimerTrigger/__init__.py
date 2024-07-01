import os
import datetime
import logging
from ..SharedCode.logger import apploger
import time
import azure.functions as func

from .fetch_scout_ip_details import ScoutToAzureStorage


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
                        tzinfo=datetime.timezone.utc
                    ).isoformat()
    
    start = time.time()
    apploger.info
    apploger.info("Function started at {}".format(datetime.datetime.now()))
    ip = "104.18.213.12"
    scout_to_azure_storage_obj = ScoutToAzureStorage(start)
    scout_to_azure_storage_obj.get_scout_ip_data(ip)
    apploger.info("Function ended at {}".format(datetime.datetime.now()))

    if mytimer.past_due:
        apploger.info('The timer is past due!')

    apploger.info('Python timer trigger function ran at %s', utc_timestamp)

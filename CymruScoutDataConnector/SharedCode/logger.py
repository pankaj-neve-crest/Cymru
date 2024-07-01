import logging
import sys

try:
    apploger = logging.getLogger("azure")
    apploger.setLevel(logging.DEBUG)
except Exception as e:
    apploger.setLevel(logging.DEBUG)
finally:
    handler = logging.StreamHandler(stream=sys.stdout)
    apploger.addHandler(handler)

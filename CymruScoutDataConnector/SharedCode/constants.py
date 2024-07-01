import os
## API Details
# Token
ScoutCymruAPIToken = "Basic amF5ZXNoLnByYWphcGF0aUBjcmVzdGRhdGEuYWk6U2VudGluZWxAMTIzNDU2"
ScouCymrutBaseURL = "https://scout.cymru.com"
ScoutCymruIPSectionsDetailsURL = "/api/scout/ip/{}/details?sections=pdns"
# URL = "https://scout.cymru.com/api/scout/ip/{}/details?sections=pdns"


# Workspace Details
WorkspaceKey = "NiI5Zux7HX13CeOLKD/kh47AtwI4pGaTC8AAWRYN0+MwdRf6xSKq8OoDGMASnOl6VITo9h9jbpemxI+ZRHLwtQ=="
WorkspaceID = "62ba18dd-4e20-4a87-a25b-e592f4d8b93c"

# MS Sentinel Table Details
IP_PDNS_TABLE_NAME = "scout_ip_pdns"

# Log Analtyics Uri
LogAnaltyicsUri = "https://{}.ods.opinsights.azure.com{}?api-version=2016-04-01"


## BLEOW CONSTANTS ARE NOT USED IN CODE.
# *Sentinel related constants
AZURE_CLIENT_ID = os.environ.get("Azure_Client_Id", "")
AZURE_CLIENT_SECRET = os.environ.get("Azure_Client_Secret", "")
AZURE_TENANT_ID = os.environ.get("Azure_Tenant_Id", "")
WORKSPACE_KEY = os.environ.get("Workspace_Key", "")
WORKSPACE_ID = os.environ.get("Workspace_Id", "")

# Cymru Scout API details
API_KEY = os.environ["CymruScoutAPIToken"]
url = os.environ["CymruScoutBaseURL"]
connection_string = os.environ["AzureWebJobsStorage"]

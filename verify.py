import requests
import json

from utils.auth import IntersightAuth, get_authenticated_aci_session
from env import config

auth=IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'],
                      api_key_id=config['INTERSIGHT_API_KEY'])

BASE_URL='https://www.intersight.com/api/v1'

url = f"{BASE_URL}/cond/Alarms"

response = requests.get(url, auth=auth)

if response.status_code == 200:
    print("Intersight access verified")
else:
    print(f"Intersight access denied. status code: {response.status_code}")

# Check for ACI simulator access
aci_session = get_authenticated_aci_session(config['ACI_USER'], config['ACI_PASSWORD'], config['ACI_BASE_URL'])

if aci_session is not None:
    print("ACI access verified")
else:
    print("Failed to verify access to ACI.")
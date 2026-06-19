from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "agent_id": "agt-f6d5c5fa",
    "version_id": "pmt-6e2ba6cbfe",
    "channel": "telephony",
    "phone_number": "917248964290",
    "external_id": "test_001",
    "recording_enabled": True,
    "voice": "Kavya"
}

response = requests.post(
    f"{BASE_URL}/api/v1/public/calls/test",
    headers=headers,
    json=payload
)

print(response.status_code)
print(json.dumps(response.json(), indent=2))
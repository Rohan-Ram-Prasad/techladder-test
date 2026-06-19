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
    "agent_name": "agt-f6d5c5fa",
    "version_name": "pmt-6e2ba6cbfe",
    "voice": "Kavya",
    "did_number_id": "08037236753",
    "interruption": True,
    "use_alternate_number": False,
    "start_mode": "immediate",
    "schedule_date": "2026-06-19",
    "schedule_time": "14:00",
    "timezone": "Asia/Kolkata",
    "contacts": [
        {
            "external_id": "101",
            "name": "Akshat",
            "phone_number": "917248964290"
        }
    ]
}

response = requests.post(
    f"{BASE_URL}/api/v1/public/call-batches",
    headers=headers,
    json=payload
)

print(response.status_code)
print(json.dumps(response.json(), indent=2))
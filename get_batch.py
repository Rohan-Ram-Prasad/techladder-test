from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(
    f"{BASE_URL}/api/v1/public/call-batches/sched_6171f8a8",
    headers=headers
)

print(response.status_code)
print(json.dumps(response.json(), indent=2))
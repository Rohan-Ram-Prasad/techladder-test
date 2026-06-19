from dotenv import load_dotenv
import os
import requests
import time
import json

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

BATCH_ID = "sched_6171f8a8"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

for i in range(24):  # 24 attempts × 5 sec = 120 sec

    response = requests.get(
        f"{BASE_URL}/api/v1/public/call-batches/{BATCH_ID}/results",
        headers=headers
    )

    data = response.json()

    print(f"Attempt {i + 1}")

    items = data.get("data", {}).get("items", [])

    if items and items[0].get("summary") is not None:
        print("PASS - Summary Found")
        print(json.dumps(data, indent=2))
        break

    print("Waiting...")
    time.sleep(5)

else:
    print("FAIL - No summary within 120 seconds")
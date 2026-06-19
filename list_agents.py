from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(
    f"{BASE_URL}/api/v1/public/agents",
    headers=headers
)

print(response.status_code)
print(response.text)
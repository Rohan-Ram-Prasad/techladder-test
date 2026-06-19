from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")


def test_authentication():

    response = requests.get(
        f"{BASE_URL}/api/v1/public/me",
        headers={
            "Authorization": f"Bearer {API_KEY}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status_code"] == 200
    assert "account_id" in data["data"]

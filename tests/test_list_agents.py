from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")


def test_list_agents():

    response = requests.get(
        f"{BASE_URL}/api/v1/public/agents",
        headers={
            "Authorization": f"Bearer {API_KEY}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status_code"] == 200
    assert len(data["data"]["items"]) > 0

    first_agent = data["data"]["items"][0]

    assert "agent_id" in first_agent
    assert "current_version" in first_agent
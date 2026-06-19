import requests
import uuid
from conftest import BASE_URL, HEADERS, AGENT_ID, VERSION_ID, PHONE_NUMBER


def test_create_batch():

    payload = {
        "agent_name": AGENT_ID,
        "version_name": VERSION_ID,
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
                "external_id": str(uuid.uuid4()),
                "name": "Automation Test",
                "phone_number": PHONE_NUMBER
            }
        ]
    }

    response = requests.post(
        f"{BASE_URL}/api/v1/public/call-batches",
        headers={**HEADERS, "Content-Type": "application/json"},
        json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data["status_code"] == 201
    assert "batch_id" in data["data"]

    print("\nBatch ID:", data["data"]["batch_id"])
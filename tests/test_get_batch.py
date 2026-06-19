import requests
from conftest import BASE_URL, HEADERS

BATCH_ID = "sched_dcfa30e0"


def test_get_batch():

    response = requests.get(
        f"{BASE_URL}/api/v1/public/call-batches/{BATCH_ID}",
        headers=HEADERS
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status_code"] == 200
    assert data["data"]["batch_id"] == BATCH_ID
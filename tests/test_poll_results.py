import requests
import time
from conftest import BASE_URL, HEADERS

BATCH_ID = "sched_dcfa30e0"


def test_poll_results():

    summary_found = False

    for _ in range(24):  # 24 × 5 sec = 120 sec

        response = requests.get(
            f"{BASE_URL}/api/v1/public/call-batches/{BATCH_ID}/results",
            headers=HEADERS
        )

        assert response.status_code == 200

        data = response.json()

        items = data.get("data", {}).get("items", [])

        if items and items[0].get("summary") is not None:
            summary_found = True
            break

        time.sleep(5)

    assert summary_found, "Summary not generated within 120 seconds"
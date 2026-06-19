from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}"
}

AGENT_ID = "agt-f6d5c5fa"
VERSION_ID = "pmt-6e2ba6cbfe"
PHONE_NUMBER = "917248964290"
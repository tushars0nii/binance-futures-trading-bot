from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

def get_client():
    client = Client(
        api_key=API_KEY,
        api_secret=SECRET_KEY
    )

    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client
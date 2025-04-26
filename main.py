from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Server is live ✅"}

@app.get("/get-price")
def get_price():
    # Dummy data (later replace with actual API response)
    return {
        "broker": "DummyBroker",
        "symbol": "EUR/USD",
        "price": 1.09876,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

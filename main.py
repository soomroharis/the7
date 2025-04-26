from fastapi import FastAPI, HTTPException
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Server is live ✅"}

@app.get("/get-price")
def get_price():
    try:
        # Dummy data (later replace with actual API response)
        return {
            "broker": "DummyBroker",
            "symbol": "EUR/USD",
            "price": 1.09876,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

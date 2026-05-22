from fastapi import FastAPI, HTTPException
import random  # <-- Mengimpor seluruh modul random

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/random/{min_value}/{max_value}")
def get_random_number(min_value: int, max_value: int):
    if min_value >= max_value:
        raise HTTPException(status_code=400, detail="Min value must be less than max value")
    # Gunakan random.randint
    return {"random_number": random.randint(min_value, max_value)}

@app.get("/random-item")
def get_random_item():
    items = ["apple", "banana", "cherry"]
    # Gunakan random.randint
    return {"random_item": items[random.randint(0, len(items) - 1)]}

from fastapi import FastAPI
from routes import checkout_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Checkout api is running"}

app.include_router(checkout_router)



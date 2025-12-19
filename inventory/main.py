from fastapi import FastAPI

from routes import prod_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Inventory api is running"}

app.include_router(prod_router)



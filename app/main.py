import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Bienvenido expectador serial, de que año quieres ver la info?: 2019 / 2020 / 2021"}
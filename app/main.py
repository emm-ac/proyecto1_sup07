from fastapi import FastAPI

app = FastAPI()


@app.get("/proyecto1_sup07")
async def index():
    return {"Hola Mundo"}
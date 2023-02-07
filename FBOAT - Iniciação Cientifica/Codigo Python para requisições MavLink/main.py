from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
async def root():
    print('Script no terminal,uvicorn main:app --reload  ,executado com sucesso ')
    return {"message": "Pedro Victor", 'idade': 24}

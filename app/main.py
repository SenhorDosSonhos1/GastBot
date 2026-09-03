from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "API do GastBot está funcionando"}
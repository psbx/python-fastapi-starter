from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Echo(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/echo")
def echo(body: Echo):
    return {"echo": body.text}

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Name(BaseModel):
    name: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/name/")
def create_name(name: Name):
    return {"message": f"Hello {name.name}!"}

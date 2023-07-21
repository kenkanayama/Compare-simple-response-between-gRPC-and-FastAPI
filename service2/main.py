import sys
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
    hello = 'hello'*100000000
    print('return size', sys.getsizeof(hello)) # だいたい470MB

    # return {"message": f"Hello {name.name}!"}
    return {"message": hello}
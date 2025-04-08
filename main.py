"""Main FastAPI app"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Returns a welcome message"""
    return {"message": "Hello World, from FastAPI"}

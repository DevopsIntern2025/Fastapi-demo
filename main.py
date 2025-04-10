"""Main FastAPI application module."""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Handles GET request to the root URL."""
    return {"message": "Hello from FastAPI. I've made changes here"}

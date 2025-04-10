"""Main FastAPI application module."""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Root endpoint returning a welcome message."""
    return {"message": "Hello from FastAPI i've made changes here"}

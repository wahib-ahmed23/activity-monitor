from fastapi import FastAPI

app = FastAPI(
    title="Activity Monitor API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "running",
        "message": "Welcome to Activity Monitor"
    }

@app.get("/health")
def health():
    return {
        "healthy": True
    }
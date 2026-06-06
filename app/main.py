from fastapi import FastAPI

app = FastAPI(title="GitHub Actions Demo API")

@app.get("/")
def read_root():
    return {"message": "Hello from GitHub Actions"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
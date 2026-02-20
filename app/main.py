from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Task Manager API", "docs": "/docs"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
    
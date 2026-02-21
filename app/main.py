from fastapi import FastAPI

app = FastAPI(
    title = "Task Manager API",
    description = "A REST API for managing tasks with JWT authentication",
    version = "1.0.0"
)

@app.get("/")
def read_root():
    return {"Message": "Task Manager API", "docs": "/docs"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
    
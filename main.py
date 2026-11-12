from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Add Prometheus metrics endpoint
Instrumentator().instrument(app).expose(app)

@app.get("/")
def read_root():
    return {"status": "healthy", "message": "CI/CD Pipeline successful"}
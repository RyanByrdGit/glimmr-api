from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import requests
import os

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/offers")
def get_mock_offers():
    offers = [
        {
            "id": "10001",
            "gpu": "RTX 3090",
            "price": "$0.25/hr",
            "ram": "24 GB"
        },
        {
            "id": "10002",
            "gpu": "A100",
            "price": "$0.65/hr",
            "ram": "40 GB"
        },
        {
            "id": "10003",
            "gpu": "RTX 4080",
            "price": "$0.45/hr",
            "ram": "16 GB"
        }
    ]
    return {"offers": offers}

@app.get("/jobs")
def get_jobs():
    mock_jobs = []  # Define mock_jobs or replace with actual data source
    return {"jobs": mock_jobs}

@app.post("/deploy")
def deploy_job():
    return {"status": "Job deployed successfully", "job_id": 1259}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mock_offers = [
    {"id": "9201685", "gpu": "RTX 3090", "price": "$0.35/hr", "ram": "11 GB"},
    {"id": "9201743", "gpu": "A5000", "price": "$0.45/hr", "ram": "24 GB"},
    {"id": "9202024", "gpu": "A100", "price": "$0.95/hr", "ram": "40 GB"},
]

mock_jobs = [
    {"id": 1258, "description": "Test image generation on offer 9201685", "status": "Succeeded"},
    {"id": 1257, "description": "Test LLM run on offer 9202024", "status": "Succeeded"}
]

@app.get("/offers")
def get_offers():
    return {"offers": mock_offers}

@app.get("/jobs")
def get_jobs():
    return {"jobs": mock_jobs}

@app.post("/deploy")
def deploy_job():
    return {"status": "Job deployed successfully", "job_id": 1259}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
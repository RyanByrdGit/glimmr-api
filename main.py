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

@app.get("/offers")
def get_real_offers():
    headers = {
        "Authorization": f"Bearer {VAST_API_KEY}"
    }
    params = {
        "verified": "true",
        "order": "dph",
        "dir": "asc",
        "limit": 5
    }
    res = requests.get("https://vast.ai/api/v0/offers", headers=headers, params=params)
    raw = res.json()
    offers = []

    for offer in raw.get("offers", []):
        offers.append({
            "id": offer.get("id"),
            "gpu": offer.get("gpu_name"),
            "price": f"${offer.get('dph_total_usd', 0):.2f}/hr",
            "ram": f"{offer.get('ram', 0)} GB"
        })

    return {"offers": offers}

@app.get("/jobs")
def get_jobs():
    return {"jobs": mock_jobs}

@app.post("/deploy")
def deploy_job():
    return {"status": "Job deployed successfully", "job_id": 1259}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
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
def get_real_offers():
    VAST_API_KEY = os.getenv("VAST_API_KEY")
    try:
        headers = {
            "Authorization": f"Bearer {VAST_API_KEY}"
        }
        params = {
            "verified": "true",
            "order": "dph",
            "dir": "asc",
            "limit": 5
        }

        res = requests.get("https://api.vast.ai/api/v0/offers", headers=headers, params=params)

        print("STATUS:", res.status_code)
        print("HEADERS:", res.headers)
        print("TEXT:", res.text)

        if "application/json" in res.headers.get("Content-Type", ""):
            raw = res.json()
        else:
            raise ValueError("Non-JSON response received")

        offers = []
        for offer in raw.get("offers", []):
            offers.append({
                "id": offer.get("id"),
                "gpu": offer.get("gpu_name"),
                "price": f"${offer.get('dph_total_usd', 0):.2f}/hr",
                "ram": f"{offer.get('ram', 0)} GB"
            })

        return {"offers": offers}
    
    except Exception as e:
        print("ERROR:", str(e))
        return JSONResponse(status_code=500, content={"error": str(e)})

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

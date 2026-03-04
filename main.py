from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 3. CORS Setup (The "Express" way)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.api_route("/api/health", methods=["GET", "HEAD"])
async def health_check():
    return {"status": "healthy", "uptime": "nominal"}

@app.post("/api/data")
async def receive_data(payload: dict):
    # FastAPI parses JSON automatically into the 'payload' dict
    return {"received": payload}
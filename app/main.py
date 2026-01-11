from app.api import predict
from fastapi import FastAPI
from app.api import predict

app = FastAPI(title="Gwanak-gu ML API")

# 무중단 배포를 위한 Liveness/Readiness Probe 엔드포인트 -2
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

app.include_router(predict.router, prefix="/api/v1")

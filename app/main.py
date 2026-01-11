from fastapi import FastAPI
from app.api import predict
from prometheus_fastapi_instrumentator import Instrumentator # 메트릭 라이브러리 추가

app = FastAPI(title="Gwanak-gu ML API")

# 1. Prometheus 메트릭 수집 및 /metrics 엔드포인트 노출 설정
# 이 코드가 추가되면 Grafana가 데이터를 가져갈 수 있는 통로가 생깁니다.
Instrumentator().instrument(app).expose(app)

# 무중단 배포를 위한 Liveness/Readiness Probe 엔드포인트
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

app.include_router(predict.router, prefix="/api/v1")
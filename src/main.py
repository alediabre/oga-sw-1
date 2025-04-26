from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from src.service.reto1 import contar_combinaciones
from src.service.reto2 import get_secuencias
from src.service.reto3 import min_movimientos
from src.schemas.container_schema import ContenedoresRequest
import yaml


app = FastAPI()
base_server = "/challenges"
internal_error_message = "Error interno inesperado por parte del servidor"

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def load_openapi_yaml():
    with open("src/openapi.yaml", "r") as f:
        openapi_schema = yaml.safe_load(f)
        app.openapi_schema = openapi_schema

@app.get(f"{base_server}/solution-1")
def solution_1(n: int = Query(..., ge=1)):
    try:
        result = contar_combinaciones(n)
        return {"result": str(result)}
    except Exception:
        raise HTTPException(status_code=500, detail=internal_error_message)

@app.get(f"{base_server}/solution-2")
def solution_2(limit: int = Query(..., ge=1)):
    try:
        result = get_secuencias(limit)
        return {"result": str(result)}
    except Exception:
        raise HTTPException(status_code=500, detail=internal_error_message)
    
@app.post(f"{base_server}/solution-3")
def solution_3(request: ContenedoresRequest):
    try:
        result = min_movimientos(request.contenedores)
        return {"result": str(result)}
    except Exception:
        raise HTTPException(status_code=500, detail=internal_error_message)

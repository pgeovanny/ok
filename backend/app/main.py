from fastapi import FastAPI
from app.routers.upload import router as upload_router
from app.routers.extract import router as extract_router

app = FastAPI(
    title="Gabarite Backend",
    description="API para upload e extração de PDFs de questões e leis"
)

# Rota raiz para evitar 404
@app.get("/")
def root():
    return {"message": "API Gabarite online!"}

# Inclui routers com prefixos
app.include_router(upload_router, prefix="/upload", tags=["Upload"])
app.include_router(extract_router, prefix="/extract", tags=["Extract"])


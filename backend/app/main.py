from fastapi import FastAPI, Response
from app.routers.upload import router as upload_router
from app.routers.questions import router as questions_router
from app.routers.law import router as law_router

app = FastAPI(
    title="Gabarite Backend",
    description="Fluxo: questões → padrão IA → lei → organização → aplicação do padrão"
)

# GET raiz
@app.get("/")
def root():
    return {"message": "API Gabarite online!"}

# HEAD raiz para health checks
@app.head("/")
def root_head():
    return Response(status_code=200)

# Inclui routers
app.include_router(upload_router, prefix="/upload", tags=["Upload"])
app.include_router(questions_router, prefix="/questions", tags=["Questions"])
app.include_router(law_router, prefix="/law", tags=["Law"])

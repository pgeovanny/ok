import os
from fastapi import APIRouter, File, UploadFile

router = APIRouter()

UPLOADS_DIR = "uploads"

@router.post("/file")
async def upload_file(file: UploadFile = File(...)):
    os.makedirs(UPLOADS_DIR, exist_ok=True)  # Garante que a pasta existe
    file_path = os.path.join(UPLOADS_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    print(f"[UPLOAD] Arquivo salvo em: {file_path}")
    return {"filename": file.filename, "path": file_path}

#  UploadFile es lo que te permite subirlo
# File es lo que te permite ponerles parametros
# os
from fastapi import FastAPI,UploadFile,File ,HTTPException

app = FastAPI()

@app.post("/subir")
async def subir(file: UploadFile = File(...)):
    contenido = await file.read()
    return {"file_name":file.filename,"file_type":file.content_type,"tamano":len(contenido)}


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()  # Lee el contenido del archivo
    tamayo = len(content) / (1024 * 1024)
    # Aquí puedes procesar el contenido
    return {"filename": file.filename, "length": tamayo}


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Validar el tipo de archivo
    allowed_types = ["image/jpeg", "image/png", "application/pdf"]
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Tipo de archivo no permitido.")

    # Leer el contenido para comprobar el tamaño
    content = await file.read()
    max_size = 2 * 1024 * 1024  # 2 MB en bytes
    if len(content) > max_size:
        raise HTTPException(status_code=400, detail="El archivo es demasiado grande.")

    # Procesar el archivo
    return {"filename": file.filename, "size": len(content)}
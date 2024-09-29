import shutil
import os
from fastapi import FastAPI, UploadFile,File

app = FastAPI()

@app.post("/subir")
async def subir(file: UploadFile = File(...)):
    saze = len(await file.read()) / (1024*1024)
    name_archivo = file.filename
    type_archivo = file.content_type
    
    os.makedirs("archivos", exist_ok=True)

    locacion = f"archivos/{name_archivo}"

    with open(locacion,"wb")  as abierto:
        shutil.copyfileobj(file.file,abierto)


    return{"name":name_archivo,"saze":saze,"type":type_archivo}







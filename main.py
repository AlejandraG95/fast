from fastapi import FastAPI

#* creamos un script Python que contenga tu aplicación FastAP

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "¡Hola, mundo!"}

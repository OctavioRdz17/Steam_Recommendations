from fastapi import FastAPI

app = FastAPI(title= 'Mi aplicación con FastAPI')

# Esta api esta alojada en 
# https://steam-recommendations-api.onrender.com


@app.get("/")# main
def read_root():
    return {"message": "Welcome to steam recommendations api!"}

# ejemplo
@app.get("/data")
def get_data():
    # Aquí puedes cargar los datos procesados y devolverlos como respuesta JSON
    # Ejemplo: return {"data": "datos_procesados"}
    pass
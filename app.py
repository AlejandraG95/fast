from uvicorn import main as uvicorn_main

#* se encargará de ejecutar el servidor FastAPI

def run_server():
    uvicorn_main(["main:app", "--host", "0.0.0.0", "--port", "8000"])

if __name__ == "__main__":
    run_server()

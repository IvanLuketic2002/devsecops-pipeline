from fastapi import FastAPI

app = FastAPI(title="DevSecOps Demo App")

@app.get("/")
def root():
    return {"message": "Secure deployment pipeline", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "ok"}

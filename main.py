from fastapi import FastAPI

app = FastAPI(title="Sarah Voice Server")

@app.get("/")
def root():
    return {"status": "ok", "service": "sarah-voice-server"}

@app.get("/health")
def health():
    return "OK"

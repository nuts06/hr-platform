from fastapi import FastAPI

# creating fastapi app
app=FastAPI()

# Health check endpoints
@app.get("/health")
def health_check():
    return {"status":"ok"}

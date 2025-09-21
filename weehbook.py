from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/tradingview-webhook")
async def tradingview_webhook(request: Request):
    data = await request.json()
    print("Received data:", data)
    # Save to file, DB, or trigger another action
    return {"status": "ok"}
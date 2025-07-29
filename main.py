from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
import os
from datetime import datetime

app = FastAPI()

@app.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()

    os.makedirs("mensagens_recebidas", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"mensagens_recebidas/msg_{timestamp}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n📩 Mensagem recebida em {timestamp}:")
    print(json.dumps(data, indent=2, ensure_ascii=False))

    return JSONResponse(content={"status": "recebido"}, status_code=200)

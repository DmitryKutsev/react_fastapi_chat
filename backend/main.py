from fastapi import FastAPI
from utils.openai_requests import audio_to_text

app = FastAPI()

@app.get("/health")
async def healthcheck():
    return {"status": "ok"} 


@app.get("/get_audio_text")
async def get_audio():
    with open("my_record.mp3", "rb") as record:
        return {"text": audio_to_text(record)}


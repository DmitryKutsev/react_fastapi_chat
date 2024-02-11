from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from utils.openai_requests import audio_to_text, get_chat_response

origins = [
    "http://localhost:5713",
    "http://localhost:5714",
    "http://localhost:3000",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def healthcheck():
    return {"status": "ok"} 


@app.get("/get_audio_text")
async def get_audio():
    with open("my_record.mp3", "rb") as record:
        return {"text": audio_to_text(record)}


@app.post("/responce_text")
async def responce_text(request_text: str):
     return JSONResponse(content={"response": get_chat_response(request_text)})
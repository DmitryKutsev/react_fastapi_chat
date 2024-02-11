import openai
from pathlib import Path

from loguru import logger
from decouple import config
import os


os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
# openai.api_key = config("OPENAI_API_KEY")
client = openai.OpenAI()


def audio_to_text(audio_file_path):
    try:
        transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file_path,
            )
        return transcript.text
    except Exception as err:
        logger.error(f"Error in audio_to_text: {err}")
        return

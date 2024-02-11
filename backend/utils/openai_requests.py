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


def get_chat_response(message_input):

    # messages = get_recent_messages()
    user_message = {
        "role": "user",
        "content": f"{message_input} ",
    }
    # messages.append(user_message)
    # print(messages)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"You are a helpful assistant translator. You knows three languages:"  # noqa: F541
                           f"Russian, Dutch and English. Provide only traslation of the given phrase" # noqa: F541
                           f"with all languages you know besides the language of the request. Example:" # noqa: F541
                           f"Request: Hello Answer: 1) English: hello 1) Russian: привет, 2) Dutch: hoi", # noqa: F541
            },
            user_message,
        ],
    )
    return response.choices[0].message.content

import threading
import time

from flask import Flask, request

from telegram_api import send_telegram_photo_message, send_telegram_text_message, set_telegram_webhook
from utils import generate_image

app = Flask(__name__)


@app.get("/")
def handle_home():
    return "OK", 200


@app.get("/telegram")
def handle_get_telegram():
    """TODO
    [1] get a request URL
    [2] form our webhook URL
    [3] set the webhook on Telegram server
    """
    base_url = request.base_url
    parts = base_url.split("://")[1:]
    base_url = f"""https://{"".join(parts)}"""
    set_telegram_webhook(url=base_url)
    return "OK", 200


def call_dalle_send_image(prompt: str, recipient_id: str):
    """TODO
    [1] generate the image
    [2] send the image as photo
    """
    urls = generate_image(prompt=prompt)
    for url in urls:
        send_telegram_photo_message(recipient_id=recipient_id, photo_url=url)
        time.sleep(1)
    return None


@app.post("/telegram")
def handle_post_telegram():
    """TODO
    [1] receive a new message
    [2] extract the prompt
    [3] create a new thread, pass the prompt and user info
    [4] send the message OK to Telegram server

    Telegram command
    /start
    /image a flying horse
    """
    try:
        body = request.get_json()
        query = str(body["message"]["text"])
        recipient_id = body["message"]["from"]["id"]
        command = query.split(" ")[0]
        if command == "/start":
            send_telegram_text_message(
                recipient_id=recipient_id, message="Welcome, generate image using /image followed by your prompt.")
        elif command == "/image":
            words = query.split(" ")
            prompt = " ".join(words[1:])
            threading.Thread(
                target=call_dalle_send_image,
                args=[prompt, recipient_id]
            ).start()
            send_telegram_text_message(
                recipient_id=recipient_id, message="Started the image generation.")
        else:
            send_telegram_text_message(
                recipient_id=recipient_id, message="Generate image using /image followed by your prompt.")
    except:
        print("Error at /telegram POST.")
    return "OK", 200

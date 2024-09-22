import requests

import config

BASE_URL = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_API_KEY}"


def set_telegram_webhook(url: str) -> None:
    json = {"url": url}
    headers = {"Content-Type": "application/json"}
    response = requests.request(
        method="POST",
        url=f"{BASE_URL}/setWebhook",
        json=json,
        headers=headers
    )
    if response.status_code == 200:
        response = response.json()
        if response["ok"]:
            print("WEBHOOK SET")
        else:
            print("WEBHOOK NOT SET")
    else:
        print("WEBHOOK NOT SET")


def send_telegram_text_message(recipient_id: str, message: str) -> None:
    json = {"chat_id": recipient_id, "text": message}
    headers = {"Content-Type": "application/json"}
    response = requests.request(
        method="POST",
        url=f"{BASE_URL}/sendMessage",
        json=json,
        headers=headers
    )
    if response.status_code == 200:
        response = response.json()
        if response["ok"]:
            print("TELEGRAM MESSAGE SENT.")
        else:
            print("TELEGRAM MESSAGE NOT SENT.")
    else:
        print("TELEGRAM MESSAGE NOT SENT.")


def send_telegram_photo_message(recipient_id: str, photo_url: str) -> None:
    json = {"chat_id": recipient_id, "photo": photo_url}
    headers = {"Content-Type": "application/json"}
    response = requests.request(
        method="POST",
        url=f"{BASE_URL}/sendPhoto",
        json=json,
        headers=headers
    )
    if response.status_code == 200:
        response = response.json()
        if response["ok"]:
            print("TELEGRAM PHOTO MESSAGE SENT.")
        else:
            print("TELEGRAM PHOTO MESSAGE NOT SENT.")
    else:
        print("TELEGRAM PHOTO MESSAGE NOT SENT.")

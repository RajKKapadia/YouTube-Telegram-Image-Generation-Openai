import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TELEGRAM_BOT_API_KEY = os.getenv("TELEGRAM_BOT_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

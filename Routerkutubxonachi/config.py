import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
_admins_raw = os.getenv("ADMINS", "")
ADMINS = list(map(int, _admins_raw.split(","))) if _admins_raw.strip() else []

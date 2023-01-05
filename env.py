import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "5484962").strip()
API_HASH = os.getenv("API_HASH", "fae1c43de01a54ca65f738ebf931862d").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "5382236039:AAG8gnIWxkekPUF3JU5dmIx2sYg5OIrJuhY").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")

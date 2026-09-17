import os
import sys
from os import getenv


def _require_int(name: str) -> int:
    """Reads a required integer environment variable, exiting with a clear
    error message instead of a cryptic ValueError if it's missing/invalid."""
    raw = os.environ.get(name, "").strip()
    if not raw:
        sys.exit(f"❌ {name} is missing — set it in your environment variables.")
    try:
        return int(raw)
    except ValueError:
        sys.exit(f"❌ {name} must be a number, got: {raw!r}")


def _require_str(name: str) -> str:
    raw = os.environ.get(name, "").strip()
    if not raw:
        sys.exit(f"❌ {name} is missing — set it in your environment variables.")
    return raw


# ------------------------------------------------
API_ID = _require_int("API_ID")
# ------------------------------------------------
API_HASH = _require_str("API_HASH")
# ------------------------------------------------
BOT_TOKEN = _require_str("BOT_TOKEN")
# ------------------------------------------------
BOT_USERNAME = _require_str("BOT_USERNAME")
BOT_TEXT = ":𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®:"
# ------------------------------------------------
OWNER_ID = _require_int("OWNER_ID")
# ------------------------------------------------
SUDO_USERS = list(map(int, getenv("SUDO_USERS", str(OWNER_ID)).split()))
# ------------------------------------------------
# //LOG CHANNEL ID
CHANNEL_ID = _require_int("CHANNEL_ID")

# //FORCE_CHANNEL_ID
CHANNEL_ID2 = _require_int("CHANNEL_ID2")
# ------------------------------------------------
MONGO_URL = _require_str("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = _require_int("PREMIUM_LOGS")
# -----------------------------------------------
join = '<a href="">✳️ JOIN BACKUP</a>'
# -----------------------------------------------
UNSPLASH_ACCESS_KEY = 'RabDRmuXXBobanmwwbvpP5LwoG4J8ox34y5Sstz-9jk'
# -----------------------------------------------
UNSPLASH_QUERY = 'animal baby'
# -----------------------------------------------
ADMIN_BOT_USERNAME = ""  # without @

THUMB_URL = os.environ.get("THUMB_URL", "https://i.ibb.co/DPCmWSKV/1000003297-3.png")

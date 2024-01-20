from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "29167512")
APP_HASH = os.environ.get("APP_HASH", "4c9ec8f8fc4989491e71fcff719008bd")
SESSION = os.environ.get("SESSION")
ma515 = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
ma515.start()

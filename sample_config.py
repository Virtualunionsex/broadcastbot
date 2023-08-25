#  !/usr/bin/env python3
#  Author   : Renjith Mangal| shabib-k

import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6697713258:AAFDfdivj4INPJVDlfI_k7APbYxds4wmGbs")
    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "22825629"))
    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "e8db542482a1638b4e5b03ed1ddae521")
    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://jncqeegk:vp28D-Z-omAp8V7uh5bi4B5LlsYlL3nn@tyke.db.elephantsql.com/jncqeegk")
    # List of admin user ids for special functions(
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6404342282").split())


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

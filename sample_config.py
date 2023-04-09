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
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6278243144:AAFugrKWisjrTXTrbnX3e7c4W9wVxjASptY")
    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "16246834"))
    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "29b3ffa9245c07f05375b92f38e8f13d")
    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgresql://pfewsazv:NFJuP00vvb9dup3vS8jzp0ZpNYusWXtS@raja.db.elephantsql.com/pfewsazv")
    # List of admin user ids for special functions(
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1715348447").split())


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

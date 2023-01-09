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
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5697059470:AAFVogFk4IsTKht41DstaQtqGnRISuHTpOE")
    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "14672956"))
    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "115e8242ea0423893160bb61a9e05eab")
    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "mongodb://mongo:7v3wJ3rp2QCdI24J02hJ@containers-us-west-55.railway.app:7269")
    # List of admin user ids for special functions(
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5166575484").split())


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

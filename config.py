#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5979195960:AAEg9S8eYXAB-qgXjEH2L_VoS6hiEhaRZwU")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "26930530"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "b578cec1f4f5164d952c5a785a399a73")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "AQBFtiSsRL6rOl7lGpJubSjhblA2nynwI45s-MYDYzQEJP-kUosTrrFHBXv6njIwbePFdaaozreiZrdyZMyfu_bvcCX_2uRRBlyb3CGZoPtcGhkVtoMuMx3l7A579yjLDdPvLhtc41pUe7Wsrs6E7xpVaBmcxTxWyaDqvEvTfwYmqOT7TqaBnTtfljn4R7hru6LVuYFTp7lmaJbLxHGABdLRWm6pCzJNRc5-AhDHfjNGNUUyR0vXgqUAFBoHp0Limq9pG5WqVZmGUfojELQBn18HFuZT8eXXjTABYD-JWnju-C4bimVwXaNMrYaue4sGwxXxashKJqTX3Zcn1GcO8trGAAAAAVpFz-cA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://bnlwbztq:BVi0Fhbpcixt_l7dC8WH7JbVkJHxX3un@arjuna.db.elephantsql.com/bnlwbztq")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

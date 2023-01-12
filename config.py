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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "AQBYqtdf1xab4kj11EPyo2A6CQv_Dzgw9Uf1WSTml7q9kupsa6qjZPrM8_IM_qTPEtElp8vCbl4dNR1dQHaihM2jrksfgl1b4U0ck5CEUMg6pvX17DMO67-hDioM0Q1uKbuDVuvmK0e4YAYTAUXsqdb0-ZWt4hgfvuFNDESgO1LQtZU15jA7jJOjdlEfFpjgX4J5ZCA0fDUIrO4bxL2u9rB1SS6Tm41mXMarlAvKAw3agbWUg9bv3Sw4suJCUKiMy7TXLnfwteSQvQY9bKs7ezT4-rJj7V5cVP2l0DwDZFwIpPFCkPHyC3Girk3W28CBIkDV9nyKYiNX8Fqf8sP6ImAAAAAVpFz-cA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://bnlwbztq:BVi0Fhbpcixt_l7dC8WH7JbVkJHxX3un@arjuna.db.elephantsql.com/bnlwbztq")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

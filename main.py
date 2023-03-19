
from telegram_helpers import send_message
from tgtg_helpers import get_items, log_in
from json import load


def load_config() -> dict:
    try:
        f = open("config.json", mode="r+")
        config = load(f)
        f.close()
    except:
        print("Config-File missing. Run init.py first.")
        exit(1)
    return config


def process():
    try:
        config = load_config()
        credentials = config["tgtg"]
        bot_config = config["telegram"]

        client = log_in(credentials=credentials)
        while True:
            items = get_items(client=client)

            send_message(items=items, bot_config=bot_config)
    except:
        process()
        print("Some error occurred")


if __name__ == "__main__":
    process()

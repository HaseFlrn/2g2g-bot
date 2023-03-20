
from telegram_helpers import send_message, telegram_bot_sendtext
from tgtg_helpers import get_items, log_in
from tgtg import TgtgAPIError
from json import load, loads
from time import localtime, sleep


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
        last_items = []
        while True:
            if not isOutsideWorkingHours():
                items = get_items(client=client)
                if(items != last_items):
                    last_items = items
                    send_message(items=items, bot_config=bot_config)
            sleep(5*60)  # Sleep 5 minutes
    except TgtgAPIError as inst:
        statusCode, content = inst.args
        content = loads(content)
        url = content["url"]
        telegram_bot_sendtext(message="Got statusCode {}, with content {}".format(statusCode, url),
                              bot_config=load_config()["telegram"])
    except Exception as exception:
        telegram_bot_sendtext(message="Bot is broken! Fix it! {}".format(exception),
                              bot_config=load_config()["telegram"])
    except:
        telegram_bot_sendtext(message="Bot is broken! Fix it! Unknown Exception",
                              bot_config=load_config()["telegram"])


def isOutsideWorkingHours():
    (_, _, _, tm_hour, _, _, _, _, _) = localtime()
    return tm_hour < 7 or tm_hour > 21


if __name__ == "__main__":
    process()

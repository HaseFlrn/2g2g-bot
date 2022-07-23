import requests


def telegram_bot_sendtext(message: str, bot_config: dict) -> None:
    if(message != ""):
        send_text: str = "https://api.telegram.org/bot" + \
            bot_config["token"] + "/sendMessage?chat_id=" + \
            bot_config["chat_id"] + "&parse_mode=Markdown&text=" + message
        res = requests.get(send_text)


def build_restock_message(entry: dict) -> str:
    message = entry["display_name"] + ' has items! Right now ' + str(entry["items_available"]) + ' in ' + entry["address"] + '.\n' + \
        str(entry["price"]["minor_units"]/100) + entry["price"]["code"] + \
        '/' + str(entry["value"]["minor_units"]/100) + \
        entry["value"]["code"] if entry["items_available"] > 0 or entry["new_item"] == True else ""
    return message


def send_message(items: list, bot_config: dict) -> None:
    for entry in items:
        telegram_bot_sendtext(message=build_restock_message(
            entry=entry), bot_config=bot_config)

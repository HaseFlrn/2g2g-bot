import requests


def telegram_bot_sendtext(message: str, bot_config: dict):
    send_text = "https://api.telegram.org/bot" + \
        bot_config["token"] + "sendMessage?chat_id=" + \
        bot_config["chat_id"] + "&parse_mode=Markdown&text=" + message
    res = requests.get(send_text)

def build_restock_message(entry: dict):
    message = entry["display_name"] + ' has restock! Right now ' + entry["items_available"] + ' in ' + entry["address"] + '.\n' + \
        (entry["price"]["minor_units"]/100) + entry["price"]["code"] + '/' + (entry["value"]["minor_units"]/100) + entry["value"]["code"]
    return message
import requests


def telegram_bot_sendtext(message: str, bot_config: dict):
    send_text = "https://api.telegram.org/bot" + \
        bot_config["token"] + "sendMessage?chat_id=" + \
        bot_config["chat_id"] + "&parse_mode=Markdown&text=" + message
    res = requests.get(send_text)

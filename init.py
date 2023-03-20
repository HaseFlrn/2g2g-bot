
from tgtg import TgtgClient, TgtgPollingError
import json


def fillJSON(email: str, creds: dict, token="", chat_id="") -> dict:
    return {
        'tgtg': {
            'email': email,
            'access_token': creds["access_token"],
            'refresh_token': creds["refresh_token"],
            'user_id': creds["user_id"],
            "cookie": creds["cookie"]
        },
        'telegram': {
            'token': token,
            'chat_id': chat_id
        }
    }


try:
    email = input("Please enter your email:")
    client = TgtgClient(email=email)
    creds = client.get_credentials()

    try:
        with open("config.json", mode="r+") as f:
            dic = json.load(f)
            telegramDic = dic["telegram"]
        f.close()

        d = fillJSON(email=email, creds=creds["tgtg"],
                     token=telegramDic["token"], chat_id=telegramDic["chat_id"])
    except:
        d = fillJSON(email=email, creds=creds)

    with open("config.json", "w") as f:
        f.write(json.dumps(d))
    f.close()
    
    print("Done! Now open the config.json file and add your telegram credentials. Then you can run main.py and enjoy your tgtg-Telegram bot!")
except TgtgPollingError:
    print("Your email is not linked to a tgtg account. Please signup with this email first.")
except:
    print("An error occurred!")

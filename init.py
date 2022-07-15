
from tgtg import TgtgClient, TgtgPollingError
import json

try:
    email = input("Please enter your email:")
    client = TgtgClient(email=email)
    creds = client.get_credentials()
    d = {
        'tgtg': {
            'email': email,
            'access_token': creds["access_token"],
            'refresh_token': creds["refresh_token"],
            'user_id': creds["user_id"]
        },
        'telegram': {
            'token': '',
            'chat_id': ''
        }
    }
    with open("config.json", "w") as f:
        f.write(json.dumps(d))
    print("Done! Now open the config.json file and add your telegram credentials. Then you can run main.py and enjoy your tgtg-Telegram bot!")
except TgtgPollingError:
    print("Your email is not linked to a tgtg account. Please signup with this email first.")
except:
    print("An error occurred!")

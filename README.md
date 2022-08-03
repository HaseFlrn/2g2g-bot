# 2g2g-bot

## Problem

I love to use the [2good2go-app](https://toogoodtogo.com/en-us). The only problem that troubles me, is that yoou won't get notified when your favourite stores have restocked.

## Solution

I use the [2good2go Python library](https://pypi.org/project/tgtg/) to get notified via Telegram (more might follow).
To set up your own Telegram Bot use [this](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e) guide.
Since I'm running this script on my Raspberry Pi, I use CronTab to schedule the automated runs. [Here](https://towardsdatascience.com/how-to-schedule-python-scripts-with-cron-the-only-guide-youll-ever-need-deea2df63b4e) you can find a good guide about how to use CronTab.

## Getting Started

Make sure you installed and configured python3 and pip correctly.
Then run:
```sh
pip install -r /path/to/requirements.txt
```

Run the [init.py](init.py) script first and follow the steps (Opening your mailbox on Desktop or a Device without 2g2g-App before might come handy).
```sh
python3 init.py
```

The script will generate a config.json with your TooGoodToGo credentials.
Afterwards follow the steps of the [Telegram Bot guide](ttps://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e) and add the credentials to the respective keys.  
In case you also want to use CronTab, you can use the [linked guide](https://towardsdatascience.com/how-to-schedule-python-scripts-with-cron-the-only-guide-youll-ever-need-deea2df63b4e) to find out how it works.
Else you can also edit the [main.py](main.py) script and add a python package like [schedule](https://pypi.org/project/schedule/) to schedule your runs and run:
```sh
python3 main.py
```

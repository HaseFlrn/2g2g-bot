# 2g2g-bot

## Problem

I love to use the [2good2go-app](https://https://toogoodtogo.com/en-us). The only problem that troubles me, is that yoou won't get notified when your favourite stores have restocked.

## Solution

I use the [2good2go Python library](https://pypi.org/project/tgtg/) to get notified via Telegram (more might follow).
To set up your own Telegram Bot use [this](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e) guide.
Since I'm running this script on my Raspberry Pi, I use CronTab to schedule the automated runs. [Here](https://towardsdatascience.com/how-to-schedule-python-scripts-with-cron-the-only-guide-youll-ever-need-deea2df63b4e) you can find a good guide about how to use CronTab.

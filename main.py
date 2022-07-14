
from tgtg_helpers import log_in
from json import load
import json


def load_config() -> dict:
    try:
        f = open("config.json", mode="r+")
        config = load(f)
        f.close()
    except:
        print("Config-File missing. Run init.py first.")
        exit(1)
    return config

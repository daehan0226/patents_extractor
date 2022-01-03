import json

config = None
with open("./config/config.json", encoding="utf-8") as json_file:
    config = json.load(json_file)

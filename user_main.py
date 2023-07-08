import json
from s.ws_start_user import *
from s.auto1 import *

with open('setting.json') as f:
    setting = json.load(f)
start(scream=setting["scream"])


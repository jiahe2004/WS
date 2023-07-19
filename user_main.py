# -*- coding: utf-8 -*-
import json
from s import *
import os



os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open('setting.json') as f:
    setting = json.load(f)

if __name__ == '__main__':
    WS = WSTK(setting=setting)
    WS.menu()

    
    


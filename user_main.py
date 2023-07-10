# -*- coding: utf-8 -*-
import tkinter as tk
import json
from PIL import Image,ImageTk
from s import *
import os

button = button()


os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open('setting.json') as f:
    setting = json.load(f)

if __name__ == '__main__':
    WS = tk.Tk()
    WSTK.start(WS,setting)
    
    


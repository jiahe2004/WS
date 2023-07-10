# -*- coding: utf-8 -*-
import tkinter as tk
import json
from PIL import Image,ImageTk
from s.auto1 import *
from s.button import *
import os
import cv2

button = button()


os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open('setting.json') as f:
    setting = json.load(f)
def wh(setting,s):
    return setting["scream"][s]

def get_img(filename,width,height):
    im = Image.open(filename).resize((width,height))
    im = ImageTk.PhotoImage(im)
    return im


class WSTK:
    def stop(WS):
        WS.quit()
    def start(WS,setting):
        WS.title("WS by XuQingTW")
        WS.geometry(wh(setting,0)+"x"+wh(setting,1))
        WS.resizable(False,False)
        WSTK.default(WS,setting)
    def default(WS,setting):
        try:
            for i in WS.winfo_children():
                i.destroy()
        except:
            pass
        background = tk.Canvas(WS,width=wh(setting,0),height=wh(setting,1))
        p = get_img(filename=".\\pic\\background.jpg",width=1280,height=720)
        background.create_image(640,360,image=p)
        background.pack()
    def menu(WS):
        print("主畫面")
    def edit_deck(WS):
        print("編輯牌組")
    def battle(WS):
        print("戰鬥畫面")

        


        
        


if __name__ == '__main__':
    WS = tk.Tk()
    WSTK.start(WS,setting)
    
    


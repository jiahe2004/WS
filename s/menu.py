import PIL.Image,PIL.ImageTk
import tkinter as tk

def wh(setting,s):
    return setting["scream"][s]

def get_img(filename,width,height):
    im = PIL.Image.open(filename).resize((width,height))
    im = PIL.ImageTk.PhotoImage(im)
    return im

from tkinter import *

class WSTK():
    def __init__(self,setting):
        self.WS = tk.Tk()
        self.set = setting
    def stop(self):
        self.WS.quit()
    def start(self):
        self.WS.title("WS by XuQingTW")
        self.WS.geometry(str(wh(self.set,0))+"x"+str(wh(self.set,1)))
        self.WS.resizable(False,False)
        WSTK.default(self)
    def default(self):
        try:
            for i in self.WS.winfo_children():
                i.destroy()
        except:
            pass
        background = tk.Canvas(self.WS,width=wh(self.set,0),height=wh(self.set,1))
        p = get_img(filename=".\\pic\\background01.jpg",width=wh(self.set,0),height=wh(self.set,1))
        background.create_image(int(wh(self.set,0)/2),int(wh(self.set,1)/2),image=p)
        background.pack()
        self.WS.mainloop()
    def menu(self):
        print("主畫面")
    def edit_deck(self):
        print("編輯牌組")
    def battle(self):
        print("戰鬥畫面")
    def to_set_a_menu():
        print("設定畫面")
    def to_set():
        print("還沒想好")





if __name__ == '__main__':
    WS = WSTK({"scream":[1536,840]})
    WS.start()
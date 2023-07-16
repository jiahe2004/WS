import PIL.Image,PIL.ImageTk
import tkinter as tk
import cv2
from tkinter import *
def wh(setting,s):
    return setting["scream"][s]

def get_img(filename,width,height):
    im = PIL.Image.open(filename).resize((width,height))
    im = PIL.ImageTk.PhotoImage(im)
    return im



class WSTK():
    def __init__(self,setting):
        self.WS = tk.Tk()
        self.set = setting
    def set_background(self):
        background = tk.Canvas(self.WS,width=wh(self.set,0),height=wh(self.set,1))
        p = get_img(filename=".\\pic\\background01.jpg",width=wh(self.set,0),height=wh(self.set,1))
        return background , p
    def stop(self):
        self.WS.quit()
    def clear(self):
        print("clear")
        for i in self.WS.winfo_children():
            if str(i) == ".!canvas":
                pass
            else:
                i.destroy()
    def start(self):
        self.WS.title("WS by XuQingTW")
        self.WS.geometry(str(wh(self.set,0))+"x"+str(wh(self.set,1)))
        self.WS.resizable(False,False)
        WSTK.menu(self)
    def menu(self):
        background , p =WSTK.set_background(self)
        background.create_image(int(wh(self.set,0)/2),int(wh(self.set,1)/2),image=p)
        background.place(x=0,y=0,relheight=1,relwidth=1)
        to_edit = tk.Button(self.WS,text="編輯卡組",command=lambda:WSTK.edit_menu(self))
        to_edit.pack()
        
        self.WS.mainloop()
        
    def edit_menu(self):
        print("尚未施工")
        to_edit = tk.Button(self.WS,text="編輯卡組",command=lambda:WSTK.edit_menu(self))
        to_edit.pack()
        c = tk.Button(self.WS,text="清除按鈕",command= lambda:WSTK.clear(self))
        c.pack()
        


    
    




if __name__ == '__main__':
    WS = WSTK({"scream":[1280,720]})
    WS.start()
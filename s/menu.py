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
    def __init__(self,setting=list):
        self.WS = tk.Tk()
        self.set = setting

        self.WS.title("WS by XuQingTW")
        self.WS.geometry(str(wh(self.set,0))+"x"+str(wh(self.set,1)))
        self.WS.resizable(False,False)

    def stop(self):
        self.WS.quit()
    def clear(self):
        print("clear")
        
        for i in self.WS.winfo_children():
            print(type(i),i)
            if isinstance(i,type(tk.Canvas())):
                pass
            else:
                i.destroy()
    
    def set_to_menu(self):
        

        self.background = tk.Canvas(self.WS,width=wh(self.set,0),height=wh(self.set,1))
        self.p = get_img(filename=".\\pic\\background01.jpg",width=wh(self.set,0),height=wh(self.set,1))
        self.background.create_image(int(wh(self.set,0)/2),int(wh(self.set,1)/2),image=self.p)

        self.to_battle=tk.Button(text="戰鬥畫面",font=20)
        self.to_edit=tk.Button(text="編輯排組",font=20)
        self.to_setting=tk.Button(text="設定畫面",font=20)
        self.to_github=tk.Button(text="去github網頁",font=20)

    def menu(self):
        WSTK.set_to_menu(self)
        self.background.place(x=0,y=0,relheight=1,relwidth=1)
        self.to_edit.place(relx=0.45,rely=0.65,relwidth=0.1,relheight=0.05)
        self.to_battle.place(relx=0.45,rely=0.7,relwidth=0.1,relheight=0.05)
        self.to_setting.place(relx=0.45,rely=0.75,relwidth=0.1,relheight=0.05)
        self.to_github.place(relx=0.45,rely=0.8,relwidth=0.1,relheight=0.05)

        self.to_github.destroy()
        self.to_github=tk.Button(text="去github網頁",font=20)
        self.to_github.place(relx=0.45,rely=0.8,relwidth=0.1,relheight=0.05)
        print(self.WS.winfo_screenwidth(),self.WS.winfo_screenheight())
        for i in self.WS.winfo_children():
            print(i)
        self.WS.mainloop()    
    def set_edit(self):
        print(",")
    def edit_menu(self):
        print("尚未施工")
    def set_battle_menu(self):
        """waiting"""
    def battle_menu(self):
        print("尚未施工")
        


    
    




if __name__ == '__main__':
    WS = WSTK({"scream":[1280,720]})
    WS.menu()
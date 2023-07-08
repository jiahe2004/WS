# -*- coding: utf-8 -*-
import tkinter as tk
def start(scream):
    WS = tk.Tk()
    WS.title("WS by XuQingTW")
    WS.geometry(scream)
    WS.resizable(False,False)
    test = tk.Button(text="測試")
    
    WS.mainloop()

if __name__ == '__main__':
    start("1280x720")
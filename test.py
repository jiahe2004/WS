import tkinter as tk
    

class Test():
   def __init__(self):
       self.root = tk.Tk()
       self.label=tk.Label(self.root,
                           text = "Label")
       self.buttonForget = tk.Button(self.root,
                          text = 'Click to hide Label',
                          command=lambda: self.label.destroy())
       self.buttonRecover = tk.Button(self.root,
                          text = 'Click to show Label',
                          command=lambda: self.label.pack())       
       
       self.buttonForget.pack()
       self.buttonRecover.pack()
       self.label.pack(side="bottom")
       for i in self.root.winfo_children():
           i.destroy()
       self.root.mainloop()
       

   def quit(self):
       self.root.destroy()
        
app = Test()

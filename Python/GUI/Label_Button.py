import tkinter as tk
class Application(tk.Frame):
    
    on_hit = False
    
    def __init__(self, master=None):   
        tk.Frame.__init__(self, master)
        self.pack()
        self.var = tk.StringVar()
        self.createWidgets()
        
    def createWidgets(self):
        self.lable = tk.Label(self, textvariable=self.var, bg='green', font=('Arial', 12), width=15, height=2)
        self.lable.pack()
        self.btnHit = tk.Button(self, text="hit me", command=self.btdown)
        self.btnHit.pack()
        
    def btdown(self):           
        if self.on_hit == False:
            self.on_hit = True
            self.var.set('you hit me')
        else:
            self.on_hit = False
            self.var.set('')
        
root = tk.Tk()
root.title('my window')
root.geometry('200x100')
app = Application(master=root)  
app.mainloop()

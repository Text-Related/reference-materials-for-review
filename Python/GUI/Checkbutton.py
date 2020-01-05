import tkinter as tk
class Application(tk.Frame):
    
    on_hit = False
    
    def __init__(self, master=None):   
        tk.Frame.__init__(self, master)
        self.pack()
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.createWidgets()
        
    def createWidgets(self):
        self.lable = tk.Label(self, bg='yellow', width=20, text='empty')
        self.lable.pack()
        self.check1 = tk.Checkbutton(self, text='Python', variable=self.var1, onvalue=1, offvalue=0,
                                     command=self.print_selection)
        self.check2 = tk.Checkbutton(self, text='C++', variable=self.var2, onvalue=1, offvalue=0,
                                     command=self.print_selection)
        self.check1.pack()
        self.check2.pack()
        
    def print_selection(self):
        if (self.var1.get() == 1) & (self.var2.get() == 0):
            self.lable.config(text='I love only Python ')
        elif (self.var1.get() == 0) & (self.var2.get() == 1):
            self.lable.config(text='I love only C++')
        elif (self.var1.get() == 0) & (self.var2.get() == 0):
            self.lable.config(text='I do not love either')
        else:
            self.lable.config(text='I love both')
        
root = tk.Tk()
root.title('my window')
root.geometry('200x100')
app = Application(master=root)  
app.mainloop()

import tkinter as tk
class Application(tk.Frame):
    def __init__(self, master=None):   
        tk.Frame.__init__(self, master)
        self.pack()
        self.var = tk.StringVar()
        self.createWidgets()
        
    def createWidgets(self):
        self.entry = tk.Entry(self, show=None)
        #self.entry = tk.Entry(self, show="*")
        self.entry.pack()
        self.button1 = tk.Button(self, text='insert point', width=15, height=2, command=self.insert_point)
        self.button1.pack()
        self.button2 = tk.Button(self, text='insert end', command=self.insert_end)
        self.button2.pack()
        self.text = tk.Text(self, height=2)
        self.text.pack()
        
    def insert_point(self):
        var = self.entry.get()
        self.text.insert('insert', var)
    def insert_end(self):
        var = self.entry.get()
        # self.text.insert('end', var)
        self.text.insert(2.2, var)
        
root = tk.Tk()
root.title('my window')
root.geometry('200x150')
app = Application(master=root)  
app.mainloop()

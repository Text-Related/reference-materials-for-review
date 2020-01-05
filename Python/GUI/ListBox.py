import tkinter as tk
class Application(tk.Frame):
    
    on_hit = False
    
    def __init__(self, master=None):   
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.var = tk.StringVar()
        self.lable = tk.Label(self, bg='yellow', width=4, textvariable=self.var)
        self.lable.pack()
        
        self.btnSelect = tk.Button(self, text='print selection', width=15,
              height=2, command=self.print_selection)
        self.btnSelect.pack()

        var2 = tk.StringVar()
        var2.set((11,22,33,44))
        self.listBox = tk.Listbox(self, listvariable=var2)

        list_items = [1,2,3,4]
        for item in list_items:
            self.listBox.insert('end', item)
        self.listBox.insert(1, 'first')
        self.listBox.insert(2, 'second')
        self.listBox.delete(2)
        self.listBox.pack()

        
    def print_selection(self):
        value = self.listBox.get(self.listBox.curselection())
        self.var.set(value)
        
root = tk.Tk()
root.title('my window')
root.geometry('200x200')
app = Application(master=root)  
app.mainloop()

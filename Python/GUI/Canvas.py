import tkinter as tk
class Application(tk.Frame):
    
    on_hit = False
    
    def __init__(self, master=None):   
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.canvas = tk.Canvas(self, bg='blue', height=350, width=300)
        self.image_file = tk.PhotoImage(file='ins.gif')
        image = self.canvas.create_image(100, 100, anchor='nw', image=self.image_file)
        line = self.canvas.create_line(0, 0, 150, 150, width=3, fill='purple')
        oval = self.canvas.create_oval(10, 10, 70, 70, fill='red')
        arc = self.canvas.create_arc(30, 200, 80, 250, start=0, extent=180, fill='green')
        self.rect = self.canvas.create_rectangle(150, 30, 150+40, 30+40, fill='yellow')
        self.canvas.pack()
        self.btnHit = tk.Button(self, text="move", command=self.moveit)
        self.btnHit.pack()
        
    def moveit(self):           
        self.canvas.move(self.rect, 0, 2)
        
root = tk.Tk()
root.title('my window')
root.geometry('400x400')
app = Application(master=root)  
app.mainloop()

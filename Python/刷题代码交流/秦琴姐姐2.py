from tkinter import * 
root = Tk()
root.title('提出问题')
root.geometry('500x100+500+200')

def sayHi():
    messagebox.showinfo("得出结论","漂亮的吓死人") 

btnSayHi = Button(root, text="秦琴姐姐好看吗？", command=sayHi) 
btnSayHi.pack() 
root.mainloop()

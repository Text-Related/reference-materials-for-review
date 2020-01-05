import tkinter as tk
def resize(ev=None):  
	label.config(font='Helvetica -{0} bold'.format(scale.get())) 
root = tk.Tk()   #主窗口
root.geometry('600x400')  #设置了主窗口的初始大小600x400
label = tk.Label(root,text='Hello world!',font='Helvetica -12 bold')  
label.pack(fill='y',expand='yes')
scale = tk.Scale(root,from_=10,to=40,orient=tk.HORIZONTAL,command=resize) 
scale.set(12)  
scale.pack(fill='x',expand='yes')
quit = tk.Button(root,text='QUIT',command=root.quit,activeforeground='white',
activebackground = 'red')
quit.pack()
root.mainloop()

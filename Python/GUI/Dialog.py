#  -*- coding: utf-8 -*-

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit_me():
    tk.messagebox.showinfo(title='showinfo', message='连接成功')
    tk.messagebox.showwarning(title='showwarning', message='磁盘碎片过多！')
    tk.messagebox.showerror(title='showerror', message='无法连接')
    print(tk.messagebox.askquestion(title='askquestion', message='是否放弃修改的内容？'))   # return 'yes' , 'no'
    print(tk.messagebox.askyesno(title='askyesno', message='是否放弃修改的内容？'))   # return True, False
    print(tk.messagebox.askretrycancel(title='askretrycancel', message='系统忙，是否重试？'))   # return True, False
    print(tk.messagebox.askokcancel(title='askokcancel', message='是否放弃修改的内容？'))   # return True, False

tk.Button(window, text='hit me', command=hit_me).pack()
window.mainloop()

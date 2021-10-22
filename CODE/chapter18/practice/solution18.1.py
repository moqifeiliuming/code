import tkinter as tk
from tkinter import messagebox  # import this to fix messagebox error
import pickle

window = tk.Tk()
window.title('登录窗口')
window.geometry('450x200')



# user information
tk.Label(window, text='User name: ').place(x=50, y= 10)
tk.Label(window, text='Password: ').place(x=50, y= 50)

var_usr_name = tk.StringVar()
var_usr_name.set('geekori')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=10)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=50)

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    if usr_name == 'geekori' and usr_pwd == '1234':
        tk.messagebox.showinfo(title='登录', message='登录成功')
    else:
        tk.messagebox.showerror(message='用户名或密码错误！')

btn_login = tk.Button(window, text='登录', command=usr_login)
btn_login.place(x=180, y=90)
btn_cancel = tk.Button(window, text='取消', command=window.quit)
btn_cancel.place(x=250, y=90)


window.mainloop()

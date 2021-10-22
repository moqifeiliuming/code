
import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit_me():
    tk.messagebox.showinfo(title='信息对话框', message='这是我要的信息')   # return 'ok'
    tk.messagebox.showwarning(title='警告对话框', message='这是警告信息')   # return 'ok'
    tk.messagebox.showerror(title='错误对话框', message='这是错误信息')   # return 'ok'
    print(tk.messagebox.askquestion(title='询问对话框', message='你要干嘛？'))   # return 'yes' , 'no'
    print(tk.messagebox.askyesno(title='yes/no', message='请给出你的选择'))   # return True, False
    print(tk.messagebox.askokcancel(title='ok/cancal', message='确定/取消'))   # return True, False
    print(tk.messagebox.askyesnocancel(title="yes/no/cancel", message="请给出你的选择"))     # return, True, False, None

tk.Button(window, text='hit me', command=hit_me).pack()
window.mainloop()

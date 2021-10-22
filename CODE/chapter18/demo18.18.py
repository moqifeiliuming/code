import tkinter as tk

window = tk.Tk()
window.title('MenuBar')
window.geometry('200x200')

label = tk.Label(window, width = 20, bg='yellow')
label.pack()
counter = 0
def menuClick():
    global counter
    label.config(text='第 '+ str(counter) + ' 次点击')
    counter+=1

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label='文件', menu=filemenu)
filemenu.add_command(label='新建', command=menuClick)
filemenu.add_command(label='打开', command=menuClick)
filemenu.add_command(label='保存', command=menuClick)
filemenu.add_separator()
filemenu.add_command(label='退出', command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='编辑', menu=editmenu)
editmenu.add_command(label='剪切', command=menuClick)
editmenu.add_command(label='复制', command=menuClick)
editmenu.add_command(label='粘贴', command=menuClick)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='导入', menu=submenu)
submenu.add_command(label="导入文本文件", command=menuClick)
submenu.add_command(label="导入pdf文件", command=menuClick)

window.config(menu=menubar)

window.mainloop()

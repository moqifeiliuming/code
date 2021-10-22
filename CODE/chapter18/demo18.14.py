import tkinter as tk

window = tk.Tk()
window.title('Radiobutton控件')
window.geometry('200x200')
window['background'] = 'blue'

var = tk.StringVar()
label = tk.Label(window, bg='yellow', width=20, text='empty')
label.pack()
var.set('A')
def printSelection():
    label.config(text='你已经选择了' + var.get())
printSelection()
r1 = tk.Radiobutton(window, text='选项A',
                    variable=var, value='A',
                    command=printSelection)
r1.pack()
r2 = tk.Radiobutton(window, text='选项B',fg='yellow',
                    variable=var, value='B',
                    command=printSelection)
r2.pack()
r3 = tk.Radiobutton(window, text='选项C',
                    variable=var, value='C',fg='yellow',
                    command=printSelection)
r3.pack()
window.mainloop()
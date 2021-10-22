import tkinter as tk

window = tk.Tk()
window.title('Checkbutton控件')
window.geometry('200x200')
window['background'] = 'blue'
label = tk.Label(window, bg='yellow', width=20, text='empty')
label.pack()

def printSelection():
    text = ''
    if var1.get() == 1:
        text += ' ' + c1.cget('text')
    if var2.get() == 1:
        text += ' ' + c2.cget('text')
    if var3.get() == 1:
        text += ' ' + c3.cget('text')
    if var4.get() == 1:
        text += ' ' + c4.cget('text')
    label.config(text=text)

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
                    command=printSelection)
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0,
                    command=printSelection)
c3 = tk.Checkbutton(window, text='Kotlin', variable=var3, onvalue=1, offvalue=0,
                    command=printSelection)
c4 = tk.Checkbutton(window, text='Swift', variable=var4, onvalue=1, offvalue=0,
                    command=printSelection)

c1.pack()
c2.pack()
c3.pack()
c4.pack()


window.mainloop()

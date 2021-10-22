import tkinter as tk

window = tk.Tk()
window.title('Scale控件')
window.geometry('300x400')
window['background'] = 'blue'
label1 = tk.Label(window, bg='yellow', width=20)
label1.pack()

def printSelection1(v):
    label1.config(text='当前值：' + v)

scale1 = tk.Scale(window, label='拖我', from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, tickinterval=2, resolution=0.01, command=printSelection1)
scale1.pack(pady = 10)

label2 = tk.Label(window, bg='yellow', width=20)
label2.pack()
def printSelection2(v):
    label2.config(text='当前值：' + v)
scale2 = tk.Scale(window, label='拖我', from_=5, to=11, orient=tk.VERTICAL,
             length=200, tickinterval=2, resolution=0.01, command=printSelection2)
scale2.pack(pady = 10)

window.mainloop()
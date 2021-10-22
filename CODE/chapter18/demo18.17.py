import tkinter as tk

window = tk.Tk()
window.title('Listbox控件')
window.geometry('200x200')
window['background'] = 'blue'

var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=10, textvariable=var1)
l.pack()


var2 = tk.StringVar()
var2.set((11,22,33,44))
lb = tk.Listbox(window, listvariable=var2)
def onselect(evt):
    w = evt.widget
    value = w.get(w.curselection())
    var1.set(value)
lb.bind('<<ListboxSelect>>', onselect)
lb.selection_set(first=0)
value = lb.get(lb.curselection())
var1.set(value)


list_items = [11111,22222,3333,4444]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'Python')
lb.insert(2, 'Kotlin')
lb.insert(3, 'Swift')
lb.delete(2)
lb.pack(pady = 20)

window.mainloop()
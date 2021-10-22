import tkinter as tk  

window = tk.Tk() 
window.title('Entry控件与Text控件') 
window['background']='blue'
window.geometry("600x500+30+30")

      
entryVar1 = tk.StringVar()
def callback():
    entryVar2.set(entryVar1.get())   
entryVar1.trace("w", lambda a,b,c: callback())

entry1 = tk.Entry(window,textvariable=entryVar1,show='*')
entry1.pack(pady = 10)
entryVar2 = tk.StringVar()
entry2 = tk.Entry(window,textvariable=entryVar2)
entry2.pack(pady = 10)

text = tk.Text(window)
text.pack(pady = 10)
from PIL import Image, ImageTk
pic = Image.open('pic.png')
photo1=ImageTk.PhotoImage(pic)

text.image_create(tk.END, image=photo1)
text.tag_configure('big', font=('Arial', 25, 'bold'))
text.insert(tk.END, "臭美",'big')
ha = Image.open('ha.jpg')
photo2=ImageTk.PhotoImage(ha)
text.image_create(tk.END, image=photo2)

window.mainloop()  
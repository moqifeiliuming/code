import tkinter as tk  
import random  
      
window = tk.Tk() 
window.title('Label控件和Button控件') 
window['background']='blue'
window.geometry("300x200+30+30")          

label1 = tk.Label(window, 
    text='Hello World',  
    bg='green', font=('Arial', 12), width=20, height=2)
label1.pack()
var = tk.StringVar() 
var.set('Hello World')  
label2 = tk.Label(window, 
    textvariable=var,
    fg = 'blue',   
    bg='yellow', font=('Arial', 12), width=15, height=2)
label2.pack(pady = 20) 
onHit = False  
def hitMe():
    global onHit
    if onHit == False:     
        onHit = True
        var.set('世界你好')  
    else:      
        onHit = False
        var.set('Hello World') 
button1 = tk.Button(window, 
    text='点击我', 
    command=hitMe)     
button1.pack()
def getLabelText():
    print(var.get())
button2 = tk.Button(window, 
    text='获取Label控件的文本', 
    command=getLabelText)     
button2.pack(pady = 20)   
   


window.mainloop()  
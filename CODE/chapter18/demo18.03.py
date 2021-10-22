from tkinter import *  
  
window = Tk()
window.title('水平填充')
window['background']='blue'
window.geometry('200x100')  
  
w = Label(window, text="复仇者联盟", bg="red", fg="white")  
w.pack(fill=X)  
w = Label(window, text="正义联盟", bg="green", fg="black")  
w.pack(fill=X)  
w = Label(window, text="保卫地球", bg="yellow", fg="blue")  
w.pack(fill=X)  
mainloop() 
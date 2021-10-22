from tkinter import *  
  
window = Tk()
window.title('从左到右水平排列')
window['background']='blue'
window.geometry('400x100')  
w = Label(window, text="复仇者联盟", bg="red", fg="white")  
w.pack(padx=10,pady=10,side=LEFT)  
w = Label(window, text="正义联盟", bg="green", fg="black")  
w.pack(padx=10,pady=10,side=LEFT) 
w = Label(window, text="保卫地球", bg="yellow", fg="blue")  
w.pack(padx=10,pady=10,side=LEFT) 
mainloop() 

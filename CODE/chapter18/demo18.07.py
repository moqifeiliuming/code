from tkinter import *  
  
window = Tk()
window.title('内边距')
window['background']='blue'
window.geometry('200x300')  
w = Label(window, text="复仇者联盟", bg="red", fg="white")  
w.pack(fill=X,ipady=30,padx=10, pady=10)  
w = Label(window, text="正义联盟", bg="green", fg="black")  
w.pack(fill=X,ipadx=10,ipady=20)  
w = Label(window, text="保卫地球", bg="yellow", fg="blue")  
w.pack(fill=X,ipadx=10,padx=10, pady=10)  
mainloop() 

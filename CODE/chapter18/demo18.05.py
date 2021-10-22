from tkinter import *  
  
window = Tk()
window.title('设置垂直外边距')
window['background']='blue'
window.geometry('200x200')  
  
w = Label(window, text="复仇者联盟", bg="red", fg="white")  
w.pack(fill=X,pady=10)  
w = Label(window, text="正义联盟", bg="green", fg="black")  
w.pack(fill=X,pady=10)  
w = Label(window, text="保卫地球", bg="yellow", fg="blue")  
w.pack(fill=X,pady=10)  
mainloop() 

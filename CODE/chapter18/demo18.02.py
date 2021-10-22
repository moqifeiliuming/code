from tkinter import *  
  

window = Tk()
window.title('水平居中')
window.geometry('200x100') 
window['background']='blue'
Label(window, text="复仇者联盟", bg="red", fg="white").pack()  
Label(window, text="正义联盟", bg="green", fg="black").pack()  
Label(window, text="天启星", bg="yellow", fg="blue").pack()  
  
mainloop()  
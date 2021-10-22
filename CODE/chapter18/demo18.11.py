from tkinter import *  
window = Tk() 
window.title('grid布局') 
window['background'] = '#AAA'
window.geometry("400x150+30+30")     
colours = ['red','green','orange','white','yellow','blue']  

r = 0  

for c in colours:  
    Label(window,text=c, relief=RIDGE,width=15).grid(row=r,column=0)  
    Label(window,bg=c, relief=SUNKEN,width=10).grid(row=r,column=1)  
    Label(window,text=c, relief=RIDGE,width=15).grid(row=r,column=2)  
    r = r + 1    
mainloop()  
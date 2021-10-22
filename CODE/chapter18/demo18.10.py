import tkinter as tk  
import random  
      
window = tk.Tk() 
window.title('place布局') 
window['background']='blue'
window.geometry("180x200+30+30")          
languages = ['Python','Swift','C++','Java','Kotlin']  
labels = range(5)  
for i in range(5):  
   ct = [random.randrange(256) for x in range(3)]  
   brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))  
   ct_hex = "%02x%02x%02x" % tuple(ct)  
   bg_colour = '#' + "".join(ct_hex)  
   label = tk.Label(window,   
                text=languages[i],   
                fg='White' if brightness < 120 else 'Black',   
                bg=bg_colour)  
   label.place(x = 25, y = 30 + i*30, width=120, height=25)  
            
window.mainloop()  
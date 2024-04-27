import tkinter as tk
import time
import math

window = tk.Tk()

def digital_clock():
    hrs = time.strftime("%H")
    min = time.strftime("%M")
    sec = time.strftime("%S")
    am_pm = time.strftime("%p")
    time_text = hrs + ":" + min + ":" + sec + " " + am_pm
    digital_clock_label.config(text=time_text)
    digital_clock_label.after(1000 , digital_clock)    
    
digital_clock_label = tk.Label(window , text="00:00:00" , font="Helvetica 72 bold")
digital_clock_label.pack()   
    
digital_clock()
window.mainloop()



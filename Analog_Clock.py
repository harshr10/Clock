import tkinter as tk
import time
import math

window = tk.Tk()
window.geometry("500x500")

def analog_clock():    
    
    hrs = int(time.strftime("%I"))
    min = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))
    
    sec_x = sec_hand_len * math.sin(math.radians(sec * 6)) + center_x
    sec_y = -1 * sec_hand_len * math.cos(math.radians(sec * 6)) + center_y
    canvas.coords(sec_hand , center_x , center_y , sec_x , sec_y)

    min_x = min_hand_len * math.sin(math.radians(min * 6)) + center_x
    min_y = -1 * min_hand_len * math.cos(math.radians(min * 6)) + center_y
    canvas.coords(min_hand , center_x , center_y , min_x , min_y)
    
    hrs_x = hr_hand_len * math.sin(math.radians(hrs * 30)) + center_x
    hrs_y = -1 * hr_hand_len * math.cos(math.radians(hrs * 30)) + center_y
    canvas.coords(hr_hand , center_x , center_y , hrs_x , hrs_y)    
    
    window.after(1000 , analog_clock)
    
canvas = tk.Canvas(window , width=500 , height=500)
canvas.pack(expand=True , fill='both')
bg = tk.PhotoImage(file=r'C:\Users\New Indica\Downloads\analog_clock.png')
canvas.create_image(250, 250 , image=bg)    

center_x = 250
center_y = 250
sec_hand_len = 100
min_hand_len = 80
hr_hand_len = 70
    
sec_hand = canvas.create_line(250,250 , 250 + sec_hand_len , 250 + sec_hand_len , width=1.5 , fill='red')
min_hand = canvas.create_line(250,250 , 250 + min_hand_len , 250 + min_hand_len , width=2.5 , fill='black')
hr_hand = canvas.create_line(250,250 , 250 + hr_hand_len , 250 + hr_hand_len , width=4 , fill='black')   

analog_clock()

window.mainloop()



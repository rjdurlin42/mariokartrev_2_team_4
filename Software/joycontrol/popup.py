from tkinter import *
import time

timer = time.time()
while True:
    if time.time()-timer > 3600:
        root2 = Tk()
        root2.title("Warning")
        root2.configure(bg = "#5d23c2")
        root2.geometry('480x360-1240+1120')
        disp = Frame(root2, bg = "#5d23c2")
        disp.grid()
        star2 = Label(disp, text = "⭐⭐⭐⭐⭐", bg = "#5d23c2", fg = "gold", font = ("Orbitron", 60)).pack(side = TOP, pady=5)
        warning = Label(disp, text = "You've been playing for a while.\nWhy not take a break?", bg = "#5d23c2", fg = "gold", font = ("Orbitron", 20, "bold")).pack(side = star2, pady = 5)
        ok = Button(disp, text = " OK ", bg = "gold", fg = "#5d23c2", command=root2.destroy, font = ("Orbitron", 15, "bold")).pack(side = warning, pady = 10)
        Label(disp, text = "⭐⭐⭐⭐⭐", bg = "#5d23c2", fg = "gold", font = ("Orbitron", 60)).pack(side = ok, pady=5)
        root2.mainloop()
        timer = time.time()

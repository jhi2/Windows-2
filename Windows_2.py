from helper import *
import tkinter as tk
from tkinter import ttk
import nativesvttk
wh_monitor = tk.Tk()
SCREEN_WIDTH = wh_monitor.winfo_screenwidth()
SCREEN_HEIGHT = wh_monitor.winfo_screenheight()
wh_monitor.destroy()
DARK_WALL = "darkwall.png"
LIGHT_WALL = "lightwall2.png"
theme = "light"
DESKTOP_HEIGHT = SCREEN_HEIGHT - 20
root = tk.Tk()
close_button = tk.Button(root,text="CLOSE!",command=lambda:root.quit())
close_button.pack()
root.attributes("-fullscreen",True)
root.mainloop()
print(DESKTOP_HEIGHT)

import tkinter as tk
from PIL import ImageTk

def show_image():
    x = canvas.create_image(125, 125, image=tk_img)
    while True:
        canvas.itemconfigure(x, state=tk.NORMAL)
        button.configure(text = 'Hide')
        yield        
        canvas.itemconfigure(x, state=tk.HIDDEN)
        button.configure(text = 'Show')        
        yield

root = tk.Tk()
canvas = tk.Canvas(root, width=250, height=250)
canvas.grid(row=0, column=0)
tk_img = ImageTk.PhotoImage(file='icons8-wind-speed-43-47-50.png')

button = tk.Button(
    root, text="Show", command=show_image().__next__, anchor='w',
    width=10, activebackground="#33B5E5")
button.grid(row=1, column=0)
root.mainloop()

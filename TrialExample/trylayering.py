from tkinter import *
root = Tk()
root.title("Click me!")
def next_image(event):
    """toggle between image2 and image3"""
    global toggle_flag
    global x, y, photo2, photo3
    if toggle_flag == TRUE:
        # display photo2, same center x, y
        canvas1.create_image(x, y, image=photo2)
        toggle_flag = False
    else:
        canvas1.create_image(x, y, image=photo3)
        toggle_flag = True
    
toggle_flag = True
# pick three GIF image files you have in your working directory
# image1 is larger than image2 and image3
image1 = "Red200x200.GIF"
photo1 = PhotoImage(file=image1)
image2 = "Green100x100.GIF"
photo2 = PhotoImage(file=image2)
image3 = "Blue100x100.GIF"
photo3 = PhotoImage(file=image3)
# make canvas the size of image1/photo1
width1 = photo1.width()
height1 = photo1.height()
canvas1 = Canvas(width=width1, height=height1)
canvas1.pack()
# display photo1, x, y is center (anchor=CENTER is default)
x = (width1)/2.0
y = (height1)/2.0
canvas1.create_image(x, y, image=photo1)
canvas1.bind('<Button-1>', next_image)  # bind left mouse click
root.mainloop()

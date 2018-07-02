import tkinter as tk
from PIL import ImageTk

class Appl:
    def __init__(self):
        self.LatPx = 0
        self.LonPx = 0
    def find_px(self, Lat, Lon):
        self.LatPx = (Lat - LatN)/LatLc
        self.LonPx = (Lon - LonW)/LonLc

root = tk.Tk()
image = "MapFinal.PNG"
photo = ImageTk.PhotoImage(file = image)
width = photo.width()
height = photo.height()

LatN = 69.5
LatS = -69.3
LonE = 148.9
LonW = 1.0

LatLc = (LatS - LatN)/height
LonLc = (LonE - LonW)/width

app = Appl()
app.find_px(-69.3, 148.9)

print (app.LatPx, app.LonPx)

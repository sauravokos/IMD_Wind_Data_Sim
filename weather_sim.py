#!/usr/bin/python
# Filename: weather_sim.py
import os
import tkinter as tk
import h5py as hp
import numpy as np
import ntpath as ntp
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename



def path_leaf(path):
    head, tail = ntp.split(path)
    return tail or ntp.basename(head)



class CoordFind:


    def __init__(self):
        
        self.LatPx = 0
        self.LonPx = 0


    def find_px(self, Lat, Lon):

        self.LatPx = (Lat - LatN)/LatLc
        self.LonPx = (Lon - LonW)/LonLc




class PlottingGUI(tk.Frame):


    def __init__(self, parent, *args, **kwargs):

        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.coord = CoordFind()

        self.root = parent
        self.root.wm_title("-|-|-|-|||Wind Vector Plotter|||-|-|-|-")
        self.root.resizable(False, False)

        self.path = "None Selected"
        self.HaM = 0
        self.Lat = 0
        self.Lon = 0
        self.WiD = 0
        self.WiS = 0
        self.ima = []

        self.fr = tk.Frame(self.root, width = (width+20), height = (height+20), bd = 2)
        self.fr.grid(row = 1, column = 0)
        self.frBro = tk.Frame(self.root, width = (width+20), height = 50, bd = 2)
        self.frBro.grid(row = 0, column = 0)
        self.frHi = tk.Frame(self.root, width = (width+20), height = 50, bd = 2)
        self.frHi.grid(row = 2, column = 0)
        
        self.cv = tk.Canvas(self.fr, width = width, height = height, background = "white", bd = 0, relief = tk.SUNKEN)
        self.cv.grid(row = 0, column = 0)
        self.cv.create_image(1, 1, anchor = "nw", image = photo)

        self.broButton = tk.Button(self.frBro, text = "Browse Dsets", command = self.analyseDset, height = 3, width = 16, bg = "yellow")
        self.broButton.grid(row = 0, column = 0, padx = 20)
        self.selFile = tk.Label(self.frBro, text = self.path)
        self.selFile.grid(row = 0, column = 1)

        self.caution = tk.Label(self.frHi, text = "Optional use. Warning!!, May lead to lags in program", fg = "red")
        self.caution.grid(row = 0, column = 1)

        self.shoRedBut = tk.Button(self.frHi, text = "Show H1", command = self.show_barbs1().__next__, height = 3, width = 16, bg = "#FF0000", fg = "white", activebackground="#E533B5")
        self.shoRedBut.grid(row = 1, column = 0, padx = 7, pady = 2)
        self.shoGrnBut = tk.Button(self.frHi, text = "Show H2", command = self.show_barbs2().__next__, height = 3, width = 16, bg = "#00B400", fg = "white", activebackground="#B5E533")
        self.shoGrnBut.grid(row = 1, column = 1, padx = 7, pady = 2)
        self.shoBluBut = tk.Button(self.frHi, text = "Show H3", command = self.show_barbs3().__next__, height = 3, width = 16, bg = "#0000FF", fg = "white", activebackground="#33B5E5")
        self.shoBluBut.grid(row = 1, column = 2, padx = 7, pady = 2)

        self.desc1 = tk.Label(self.frHi, text = "100-250 hPa", fg = "white", bg = "black")
        self.desc1.grid(row = 2, column = 0)
        self.desc2 = tk.Label(self.frHi, text = "250-350 hPa", fg = "white", bg = "black")
        self.desc2.grid(row = 2, column = 1)
        self.desc3 = tk.Label(self.frHi, text = "350-700 hPa", fg = "white", bg = "black")
        self.desc3.grid(row = 2, column = 2)
        

    def analyseDset(self): 
        self.path = askopenfilename(filetypes = (("Dataset files", "*.h5")
                                                    ,("All files", "*.*") ))
        self.jfname = path_leaf(self.path)
        self.selFile = tk.Label(self.frBro, text = self.jfname)
        self.selFile.grid(row = 0, column = 1)

        self.extDset()


    def extDset(self):
        hf = hp.File(self.path, 'r')

        HaM = hf.get('HEIGHT_ASSIGNMENT_METHOD')
        Lat = hf.get('Latitude')
        Lon = hf.get('Longitude')
        WiD = hf.get('WIND_DIRECTION')
        WiS = hf.get('WIND_SPEED')

        self.HaM = np.array(HaM)
        self.Lat = np.array(Lat)/100
        self.Lon = np.array(Lon)/100
        self.WiD = np.array(WiD)
        self.WiS = np.array(WiS)

        self.BrbImR = np.empty((self.HaM.shape[0],1))
        self.BrbImG = np.empty((self.HaM.shape[0],1))
        self.BrbImB = np.empty((self.HaM.shape[0],1))



    def barb_def(self, WiS):

        if WiS < 1:
            self.ima = "1.png"
        elif WiS < 3:
            self.ima = "2.png"
        elif WiS < 8:
            self.ima = "3.png"
        elif WiS < 13:
            self.ima = "4.png"
        elif WiS < 18:
            self.ima = "5.png"
        elif WiS < 23:
            self.ima = "6.png"
        elif WiS < 28:
            self.ima = "7.png"
        elif WiS < 33:
            self.ima = "8.png"
        elif WiS < 38:
            self.ima = "9.png"
        elif WiS < 43:
            self.ima = "10.png"
        elif WiS < 48:
            self.ima = "11.png"
        elif WiS < 53:
            self.ima = "12.png" 
        elif WiS < 58:
            self.ima = "13.png"
        elif WiS < 63:
            self.ima = "14.png"
        elif WiS < 68:
            self.ima = "15.png"
        elif WiS < 73:
            self.ima = "16.png"
        elif WiS < 78:
            self.ima = "17.png"
        elif WiS < 83:
            self.ima = "18.png"
        elif WiS < 88:
            self.ima = "19.png"
        elif WiS < 93:
            self.ima = "20.png"
        elif WiS < 98:
            self.ima = "21.png"
        elif WiS < 103:
            self.ima = "22.png"
        else:
            self.ima = "23.png"


    def show_barbs1(self):
        
        self.coord = CoordFind()
        vec_im = []
        im = []
        p = []
        script_dir = os.path.dirname(os.path.abspath(__file__))        
        for i in range(0, self.HaM.shape[0]):
            self.barb_def(self.WiS[i])
            p.append("{}{}".format('Red_Barbs\\', self.ima))
            im.append(Image.open(os.path.join(script_dir, p[i])))
            w, h = im[i].size
            im[i] = im[i].resize((int(w/2), int(h/2)), Image.ANTIALIAS)
            vec_im.append(ImageTk.PhotoImage(im[i].rotate(self.WiD[i])))
        
        for i in range(0, self.HaM.shape[0]):
            if self.HaM[i] == 0:
                self.coord.find_px(self.Lat[i], self.Lon[i])
                x = self.coord.LonPx
                y = self.coord.LatPx
                self.BrbImR[i] = self.cv.create_image(x, y, image = vec_im[i])
    
        while True:
            for i in range(0, self.HaM.shape[0]):
                self.cv.itemconfigure(self.BrbImR[i], state = tk.NORMAL)
            self.shoRedBut.configure(text = "Showing H1")
            yield


    def show_barbs2(self):
        
        self.coord = CoordFind()
        vec_im = []
        im = []
        p = []
        script_dir = os.path.dirname(os.path.abspath(__file__))

        for i in range(0, self.HaM.shape[0]):
            self.barb_def(self.WiS[i])
            p.append("{}{}".format('Green_Barbs\\', self.ima))
            im.append(Image.open(os.path.join(script_dir, p[i])))
            w, h = im[i].size
            im[i] = im[i].resize((int(w/2), int(h/2)), Image.ANTIALIAS)
            vec_im.append(ImageTk.PhotoImage(im[i].rotate(self.WiD[i])))
            
        for i in range(0, self.HaM.shape[0]):
            if self.HaM[i] == 1:
                self.coord.find_px(self.Lat[i], self.Lon[i])
                x = self.coord.LonPx
                y = self.coord.LatPx
                self.BrbImG[i] = self.cv.create_image(x, y, image = vec_im[i])
                
        while True:
            for i in range(0, self.HaM.shape[0]):
                self.cv.itemconfigure(self.BrbImG[i], state = tk.NORMAL)
            self.shoGrnBut.configure(text = "Showing H2")
            yield


    def show_barbs3(self):
        
        self.coord = CoordFind()
        vec_im = []
        im = []
        p = []
        script_dir = os.path.dirname(os.path.abspath(__file__))

        for i in range(0, self.HaM.shape[0]):
            self.barb_def(self.WiS[i])
            p.append("{}{}".format('Blue_Barbs\\', self.ima))
            im.append(Image.open(os.path.join(script_dir, p[i])))
            w, h = im[i].size
            im[i] = im[i].resize((int(w/2), int(h/2)), Image.ANTIALIAS)
            vec_im.append(ImageTk.PhotoImage(im[i].rotate(self.WiD[i])))

        
        for i in range(0, self.HaM.shape[0]):
            if self.HaM[i] == 2:    
                self.coord.find_px(self.Lat[i], self.Lon[i])
                x = self.coord.LonPx
                y = self.coord.LatPx
                self.BrbImB[i] = self.cv.create_image(x, y, image = vec_im[i])
                
        while True:
            for i in range(0, self.HaM.shape[0]):
                self.cv.itemconfigure(self.BrbImB[i], state = tk.NORMAL)
            self.shoBluBut.configure(text = "Showing H3")
            yield

    


if __name__ == "__main__":

    root = tk.Tk()

    backmap = "Map.png"
    photo = ImageTk.PhotoImage(file = backmap)
    width = photo.width()
    height = photo.height()

    LatN = 69.5
    LatS = -69.3
    LonE = 148.9
    LonW = 1.0

    LatLc = (LatS - LatN)/height
    LonLc = (LonE - LonW)/width

    app = PlottingGUI(root)

    root.mainloop()

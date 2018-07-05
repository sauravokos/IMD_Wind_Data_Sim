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



class BarbDef:
    
    def choose_barb(self, winS, src):

        if winS < 1:
            BrbN = "icons8-wind-speed-less-1-50.png"
        elif winS < 3:
            BrbN = "icons8-wind-speed-1-2-50.png"
        elif winS < 8:
            BrbN = "icons8-wind-speed-3-7-50.png"
        elif winS < 13:
            BrbN = "icons8-wind-speed-8-12-50.png"
        elif winS < 18:
            BrbN = "icons8-wind-speed-13-17-50.png"
        elif winS < 23:
            BrbN = "icons8-wind-speed-18-22-50.png"
        elif winS < 28:
            BrbN = "icons8-wind-speed-23-27-50.png"
        elif winS < 33:
            BrbN = "icons8-wind-speed-28-32-50.png"
        elif winS < 38:
            BrbN = "icons8-wind-speed-33-37-50.png"
        elif winS < 43:
            BrbN = "icons8-wind-speed-38-42-50.png"
        elif winS < 48:
            BrbN = "icons8-wind-speed-43-47-50.png"
        elif winS < 53:
            BrbN = "icons8-wind-speed-48-52-50.png"
        elif winS < 58:
            BrbN = "icons8-wind-speed-53-57-50.png"
        elif winS < 63:
            BrbN = "icons8-wind-speed-58-62-50.png"
        elif winS < 68:
            BrbN = "icons8-wind-speed-63-67-50.png"
        elif winS < 73:
            BrbN = "icons8-wind-speed-68-72-50.png"
        elif winS < 78:
            BrbN = "icons8-wind-speed-73-77-50.png"
        elif winS < 83:
            BrbN = "icons8-wind-speed-78-82-50.png"
        elif winS < 88:
            BrbN = "icons8-wind-speed-83-87-50.png"
        elif winS < 93:
            BrbN = "icons8-wind-speed-88-92-50.png"
        elif winS < 98:
            BrbN = "icons8-wind-speed-93-97-50.png"
        elif winS < 103:
            BrbN = "icons8-wind-speed-98-102-50.png"
        else:
            BrbN = "icons8-wind-speed-103-107-50.png"

        self.BrbNm = "{}{}".format(src, BrbN)



class PlottingGUI(tk.Frame):


    def __init__(self, parent, *args, **kwargs):

        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.coord = CoordFind()
        self.brbn = BarbDef()

        self.root = parent
        self.root.wm_title("-|-|-|-|||Wind Vector Plotter|||-|-|-|-")
        self.root.resizable(False, False)

        self.path = "None Selected"
        self.HaM = 0
        self.Lat = 0
        self.Lon = 0
        self.WiD = 0
        self.WiS = 0

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



    def show_barbs1(self):
        
        self.coord = CoordFind()
        vec_im = tk.PhotoImage(file='~\AppData\Local\Programs\Python\Python36-32\projects\Red_Barbs\icons8-wind-speed-43-47-50.png').subsample(2)
        
        for i in range(0, self.HaM.shape[0]):
            if self.HaM[i] == 0:
                self.coord.find_px(self.Lat[i], self.Lon[i])
                x = self.coord.LonPx
                y = self.coord.LatPx
                self.BrbImR[i] = self.cv.create_image(x, y, image = vec_im)
    
        while True:
            for i in range(0, self.HaM.shape[0]):
                self.cv.itemconfigure(self.BrbImR[i], state = tk.NORMAL)
            self.shoRedBut.configure(text = "Hide H1")
            yield
            for i in range(0, self.HaM.shape[0]):
                self.cv.itemconfigure(self.BrbImR[i], state = tk.HIDDEN)
            self.shoRedBut.configure(text = "Show H1")
            yield


    def show_barbs2(self):
        
        self.coord = CoordFind()
        vec_im = tk.PhotoImage(file='~\AppData\Local\Programs\Python\Python36-32\projects\Green_Barbs\icons8-wind-speed-43-47-50.png').subsample(2)
        
        for i in range(0, self.HaM.shape[0]):
            if self.HaM[i] == 1:    
                self.coord.find_px(self.Lat[i], self.Lon[i])
                x = self.coord.LonPx
                y = self.coord.LatPx
                self.BrbImG[i] = self.cv.create_image(x, y, image = vec_im)
                
        while True:
            for i in range(0, self.HaM.shape[0]):
                self.cv.itemconfigure(self.BrbImG[i], state = tk.NORMAL)
            self.shoGrnBut.configure(text = "Hide H2")
            yield
            for i in range(0, self.HaM.shape[0]):
                self.cv.itemconfigure(self.BrbImG[i], state = tk.HIDDEN)
            self.shoGrnBut.configure(text = "Show H2")
            yield


    def show_barbs3(self):
        
        self.coord = CoordFind()
        vec_im = tk.PhotoImage(file='~\AppData\Local\Programs\Python\Python36-32\projects\Blue_Barbs\icons8-wind-speed-43-47-50.png').subsample(2)
        
        for i in range(0, self.HaM.shape[0]):
            if self.HaM[i] == 2:    
                self.coord.find_px(self.Lat[i], self.Lon[i])
                x = self.coord.LonPx
                y = self.coord.LatPx
                self.BrbImB[i] = self.cv.create_image(x, y, image = vec_im)
                
        while True:
            for i in range(0, self.HaM.shape[0]):
                self.cv.itemconfigure(self.BrbImB[i], state = tk.NORMAL)
            self.shoBluBut.configure(text = "Hide H3")
            yield
            for i in range(0, self.HaM.shape[0]):
                self.cv.itemconfigure(self.BrbImB[i], state = tk.HIDDEN)
            self.shoBluBut.configure(text = "Show H3")
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

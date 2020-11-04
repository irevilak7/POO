import tkinter

import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

import numpy as np
from math import *

def prSetTxt(pTxt, pVal):
    pTxt.delete(0, len(pTxt.get()))
    pTxt.insert(0, pVal)
# prSetTxt
    
class PlotWin:
    
    def createWindow(self):
        self.window = tkinter.Tk()
        
        self.window.title("Calc Win")
        self.window.geometry("465x250+100+200")
        
        self.lbl01 = tkinter.Label(self.window, text="Z= ")
        self.lbl01.place(x=10, y=10)
        
        self.txt01 = tkinter.Entry(self.window, bg="lightgray", width=50)
        self.txt01.place(x=50, y=10)
        prSetTxt(self.txt01, 'sin(cos(0.33*x)) + cos(sin(0.55*y))')
        
        self.btn01 = tkinter.Button(self.window, text = "Muestra", 
                                    command = self.btn01_click)
        self.btn01.place(x= 380, y=10, width=75)
        
        self.window.mainloop()
    # createWindow
    
    def showPlot(self, pFunc):
        FStr = pFunc
        #FStr = pFunc.replace("cos","math.cos")
        #FStr = FStr.replace("sin","math.sin")
        #FStr = FStr.replace("sqrt","math.sqrt")
        print(FStr)
        
        XVec = np.arange(-5, 5, 0.25)
        XSize = XVec.size
        YVec = np.arange(-5, 5, 0.25)
        YSize = YVec.size
        ZMat = np.zeros((XSize, YSize))
        
        for XIdx in range(0, XSize):
            for YIdx in range(0, YSize):
                x = XVec[XIdx]
                y = YVec[YIdx]
                z = eval(FStr)
                ZMat[XIdx, YIdx] = z
                
        XVecG, YVecG = np.meshgrid(XVec, YVec)
        #print("-----")
        #print(XVec)
        #print("-----")
        #print(XVecG)
        #print("-----")
        
        lFig = plt.figure()
        lAxis = Axes3D(lFig)
        lAxis.plot_surface(XVecG, YVecG, ZMat, 
                           rstride=1, cstride=1, cmap=cm.viridis)        
        canvas = FigureCanvasTkAgg(lFig, master=tkinter.Tk())  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    # showPlot

    def btn01_click(self):
        self.showPlot(self.txt01.get())
    # btn01_click
    
# PlotWin


if __name__ == '__main__':
    myPlotWin = PlotWin()
    myPlotWin.createWindow()

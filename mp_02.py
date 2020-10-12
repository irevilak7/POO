import tkinter

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np
from math import *

class PlotWin:
    
    def createWindow(self):
        self.window = tkinter.Tk()
        
        self.window.title("Plot")
        self.window.geometry("465x250+100+200")
    
        self.lbl01 = tkinter.Label(self.window, text="Y= ")
        self.lbl01.place(x=10, y=10)
        
        self.txt01 = tkinter.Entry(self.window, bg="lightgray", width=50)
        self.txt01.place(x=50, y=10)
    
        self.btn01 = tkinter.Button(self.window, text="Muestra",
                                    command = self.btn01_click)
        self.btn01.place(x=380, y=10, width=75)
    
        self.window.mainloop()
    # createWindows
    
    def showPlot(self):
        lPlane = Figure(figsize=(5, 4), dpi=100)
        lAxis = lPlane.add_subplot(111)
        lAxis.spines['left'].set_position('center')
        lAxis.spines['bottom'].set_position('zero')
        lAxis.spines['right'].set_color('none')
        lAxis.spines['top'].set_color('none')
        lAxis.xaxis.set_ticks_position('bottom')
        lAxis.yaxis.set_ticks_position('left')
        
        Xs = np.linspace(-5, 5, 100)
        Y = [ 2 + 0.5 * X for X in Xs ]
        lAxis.plot(Xs, Y)
        
        canvas = FigureCanvasTkAgg(lPlane, master=tkinter.Tk())
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH,
                            expand=1)
    # showPlot
    
    def btn01_click(self):
        self.showPlot()
    # btn01_click
    
# PlotWin
    
if __name__ == '__main__':
    myPlotWin = PlotWin()
    myPlotWin.createWindow()




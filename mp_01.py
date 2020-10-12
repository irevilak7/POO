
import matplotlib.pyplot as plt
import numpy as np

class PlotWin:
    
    def showPlot(self):
        lPlane = plt.figure()
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
        lPlane.show()
    # showPlot
    
# PlotWin
    
if __name__ == '__main__':
    myPlotWin = PlotWin()
    myPlotWin.showPlot()











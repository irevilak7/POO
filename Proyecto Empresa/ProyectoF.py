from tkinter import ttk
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np
from math import *

class Calc(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
    #def createWindow(self):
        #==================Ventana===================
        #self.window = tk.Tk()
        #self.window.title("Calc Win")
        #self.window2 = tk.Tk()
        #self.window.geometry("385x310+100+200")
        
        #==================Frame===================
        self.mainFrame=tk.Frame(self)
        self.mainFrame.pack()
        #==================Renglon 1===================
        #self.texto1=tk.StringVar()
        self.combobox1=ttk.Combobox(self.mainFrame)
        self.combobox1.bind("<<ComboboxSelected>>", self.comboboxAction)
        self.combobox1.grid(row=0,column=0, padx=10,pady=10,columnspan=2)
        self.combobox1["values"] = ["Trimestral", "Semestral", "Anual"]
        bttnGraficar = tk.Button(self.mainFrame,text="Graficar",width=10, command=self.ejemploBoton)
        bttnGraficar.grid(row=0, column=3, padx=10,pady=10)
        #==================Renglon 2===================
        self.label1 = tk.Label(self,text="Primer mes")
        self.label1.grid(in_=self.mainFrame, row=1, column=0, padx=10,pady=10)
        self.texto1=tk.StringVar()
        self.entrada1=tk.Entry(self, textvariable=self.texto1)
        self.entrada1.grid(in_ = self.mainFrame, row=1,column=1, padx=10,pady=5)
        
        self.label2 = tk.Label(self,text="Segundo mes")
        self.label2.grid(in_=self.mainFrame,row=1, column=2, padx=10,pady=10)
        self.texto2=tk.StringVar()
        self.entrada2=tk.Entry(self, textvariable=self.texto2)
        self.entrada2.grid(in_=self.mainFrame,row=1,column=3, padx=10,pady=10)
        
        #==================Renglon 3===================
        self.label3 = tk.Label(self,text="Tercer mes")
        self.label3.grid(in_=self.mainFrame,row=2, column=0, padx=10,pady=10)
        self.texto3=tk.StringVar()
        self.entrada3=tk.Entry(self, textvariable=self.texto3)
        self.entrada3.grid(in_=self.mainFrame,row=2,column=1, padx=10,pady=5)
        
        self.label4 = tk.Label(self,text="Cuarto mes")
        self.label4.grid(in_=self.mainFrame,row=2, column=2, padx=10,pady=10)
        self.texto4=tk.StringVar()
        self.entrada4=tk.Entry(self, textvariable=self.texto4)
        self.entrada4.grid(in_=self.mainFrame,row=2,column=3, padx=10,pady=10)
        
        #==================Renglon 4===================
        self.label5 = tk.Label(self,text="Quinto mes")
        self.label5.grid(in_=self.mainFrame,row=3, column=0, padx=10,pady=10)
        self.texto5=tk.StringVar()
        self.entrada5=tk.Entry(self, textvariable=self.texto5)
        self.entrada5.grid(in_=self.mainFrame,row=3,column=1, padx=10,pady=5)
        
        self.label6 = tk.Label(self,text="Sexto mes")
        self.label6.grid(in_=self.mainFrame,row=3, column=2, padx=10,pady=10)
        self.texto6=tk.StringVar()
        self.entrada6=tk.Entry(self, textvariable=self.texto6)
        self.entrada6.grid(in_=self.mainFrame,row=3,column=3, padx=10,pady=10)
        
        #==================Renglon 5===================
        self.label7 = tk.Label(self,text="Septimo mes")
        self.label7.grid(in_=self.mainFrame,row=4, column=0, padx=10,pady=10)
        self.texto7=tk.StringVar()
        self.entrada7=tk.Entry(self, textvariable=self.texto7)
        self.entrada7.grid(in_=self.mainFrame,row=4,column=1, padx=10,pady=5)
        
        self.label8 = tk.Label(self,text="Octavo mes")
        self.label8.grid(in_=self.mainFrame,row=4, column=2, padx=10,pady=10)
        self.texto8=tk.StringVar()
        self.entrada8=tk.Entry(self, textvariable=self.texto8)
        self.entrada8.grid(in_=self.mainFrame,row=4,column=3, padx=10,pady=10)
        
        #==================Renglon 6===================
        self.label9 = tk.Label(self,text="Noveno mes")
        self.label9.grid(in_=self.mainFrame,row=5, column=0, padx=10,pady=10)
        self.texto9=tk.StringVar()
        self.entrada9=tk.Entry(self, textvariable=self.texto9)
        self.entrada9.grid(in_=self.mainFrame,row=5,column=1, padx=10,pady=5)
        
        self.label10 = tk.Label(self,text="Decimo mes")
        self.label10.grid(in_=self.mainFrame,row=5, column=2, padx=10,pady=10)
        self.texto10=tk.StringVar()
        self.entrada10=tk.Entry(self, textvariable=self.texto10)
        self.entrada10.grid(in_=self.mainFrame,row=5,column=3, padx=10,pady=10)
        
        #==================Renglon 7===================
        self.label11 = tk.Label(self,text="Onceavo mes")
        self.label11.grid(in_=self.mainFrame,row=6, column=0, padx=10,pady=10)
        self.texto11=tk.StringVar()
        self.entrada11=tk.Entry(self, textvariable=self.texto11)
        self.entrada11.grid(in_=self.mainFrame,row=6,column=1, padx=10,pady=5)
        
        self.label12 = tk.Label(self,text="Doceavo mes")
        self.label12.grid(in_=self.mainFrame,row=6, column=2, padx=10,pady=10)
        self.texto12=tk.StringVar()
        self.entrada12=tk.Entry(self, textvariable=self.texto12)
        self.entrada12.grid(in_=self.mainFrame,row=6,column=3, padx=10,pady=10)
        
        #self.window.mainloop()

    def comboboxAction(self, event=None):
        opcion=self.combobox1.get()
        if (opcion=="Trimestral"):
            self.label4.lower(self.mainFrame)
            self.label5.lower(self.mainFrame)
            self.label6.lower(self.mainFrame)
            self.label7.lower(self.mainFrame)
            self.label8.lower(self.mainFrame)
            self.label9.lower(self.mainFrame)
            self.label10.lower(self.mainFrame)
            self.label11.lower(self.mainFrame)
            self.label12.lower(self.mainFrame)
            self.entrada4.lower(self.mainFrame)
            self.entrada5.lower(self.mainFrame)
            self.entrada6.lower(self.mainFrame)
            self.entrada7.lower(self.mainFrame)
            self.entrada8.lower(self.mainFrame)
            self.entrada9.lower(self.mainFrame)
            self.entrada10.lower(self.mainFrame)
            self.entrada11.lower(self.mainFrame)
            self.entrada12.lower(self.mainFrame)
        if (opcion=="Semestral"):
            self.label4.lift(self.mainFrame)
            self.label5.lift(self.mainFrame)
            self.label6.lift(self.mainFrame)
            self.label7.lower(self.mainFrame)
            self.label8.lower(self.mainFrame)
            self.label9.lower(self.mainFrame)
            self.label10.lower(self.mainFrame)
            self.label11.lower(self.mainFrame)
            self.label12.lower(self.mainFrame)
            self.entrada4.lift(self.mainFrame)
            self.entrada5.lift(self.mainFrame)
            self.entrada6.lift(self.mainFrame)
            self.entrada7.lower(self.mainFrame)
            self.entrada8.lower(self.mainFrame)
            self.entrada9.lower(self.mainFrame)
            self.entrada10.lower(self.mainFrame)
            self.entrada11.lower(self.mainFrame)
            self.entrada12.lower(self.mainFrame)
        if (opcion=="Anual"):
            self.label4.lift(self.mainFrame)
            self.label5.lift(self.mainFrame)
            self.label6.lift(self.mainFrame)
            self.label7.lift(self.mainFrame)
            self.label8.lift(self.mainFrame)
            self.label9.lift(self.mainFrame)
            self.label10.lift(self.mainFrame)
            self.label11.lift(self.mainFrame)
            self.label12.lift(self.mainFrame)
            self.entrada4.lift(self.mainFrame)
            self.entrada5.lift(self.mainFrame)
            self.entrada6.lift(self.mainFrame)
            self.entrada7.lift(self.mainFrame)
            self.entrada8.lift(self.mainFrame)
            self.entrada9.lift(self.mainFrame)
            self.entrada10.lift(self.mainFrame)
            self.entrada11.lift(self.mainFrame)
            self.entrada12.lift(self.mainFrame)
    def ejemploBoton(self):
            self.showPlot()
    def showPlot(self):
        lPlane = Figure(figsize=(5, 4), dpi=100)
        lAxis = lPlane.add_subplot(111)
        lAxis.spines['left'].set_position('center')
        lAxis.spines['bottom'].set_position('zero')
        lAxis.spines['right'].set_color('none')
        lAxis.spines['top'].set_color('none')
        lAxis.xaxis.set_ticks_position('bottom')
        lAxis.yaxis.set_ticks_position('left')
        opcion=self.combobox1.get()
        Xs= np.linspace(1, 3,3)
       
        
        if (opcion=="Trimestral"):
            Xs= np.linspace(1, 3,3)
            Y=[1,2,3]
            Y[0]=int(self.entrada1.get());
            Y[1]=int(self.entrada2.get());
            Y[2]=int(self.entrada3.get());
            
        elif (opcion=="Semestral"):
            Xs= np.linspace(1, 6,6)
            Y=[1,2,3,4,5,6]
            Y[0]=int(self.entrada1.get());
            Y[1]=int(self.entrada2.get());
            Y[2]=int(self.entrada3.get());
            Y[3]=int(self.entrada4.get());
            Y[4]=int(self.entrada5.get());
            Y[5]=int(self.entrada6.get());
        else :
            Xs= np.linspace(1, 12,12)
            Y=[1,2,3,4,5,6,7,8,9,10,11,12]

        lAxis.bar(Xs, Y)
        
        canvas = FigureCanvasTkAgg(lPlane, master=tk.Tk())
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            
        

    #Creamos la calculadora
if __name__ == '__main__':
    myCalc = Calc()
    myCalc.mainloop()
    
    
    
    
    
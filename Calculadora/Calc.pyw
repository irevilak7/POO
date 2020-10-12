# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:11:42 2020

@author: LuisJesús
"""
import tkinter

class Calc:
    
    def __init__(self):
        self.aNumIdx=1;
        self.aOper=''
    def createWindow(self):
        #==================Ventana===================
        self.window = tkinter.Tk()
        self.window.title("Calc Win")
        #self.window2 = tkinter.Tk()
        #self.window.geometry("385x310+100+200")
        
        #==================Frame===================
        self.mainFrame=tkinter.Frame(self.window)
        self.mainFrame.pack()
        #==================Entrada 1===================
        self.entrada1=tkinter.Entry(self.mainFrame)
        self.entrada1.grid(row=0,column=0, padx=10,pady=10,columnspan=4)
        self.entrada1.config(background="black",fg="#03f943", justify="right")
        
        #==================Entrada 2===================
        self.entrada2=tkinter.Entry(self.mainFrame)
        self.entrada2.grid(row=1,column=0, padx=10,pady=5,columnspan=4)
        self.entrada2.config(background="black",fg="#03f943", justify="right")
        
        #==================Entrada 3===================
        self.entrada3=tkinter.Entry(self.mainFrame)
        self.entrada3.grid(row=2,column=0, padx=10,pady=10,columnspan=4)
        self.entrada3.config(background="black",fg="#03f943", justify="right")
        
        #==================Fila 1===================
        self.bttn7=tkinter.Button(self.mainFrame,text="7",width=3)
        self.bttn7.grid(row=3,column=0, padx=2,pady=2)
        
        self.bttn8=tkinter.Button(self.mainFrame,text="8",width=3)
        self.bttn8.grid(row=3,column=1, padx=2,pady=2)
        
        self.bttn9=tkinter.Button(self.mainFrame,text="9",width=3)
        self.bttn9.grid(row=3,column=2, padx=2,pady=2)
        
        self.bttnDiv=tkinter.Button(self.mainFrame,text="/",width=3)
        self.bttnDiv.grid(row=3,column=3, padx=2,pady=2)
        
        #==================Fila 2===================
        self.bttn4=tkinter.Button(self.mainFrame,text="4",width=3)
        self.bttn4.grid(row=4,column=0, padx=2,pady=2)
        
        self.bttn5=tkinter.Button(self.mainFrame,text="5",width=3)
        self.bttn5.grid(row=4,column=1, padx=2,pady=2)
        
        self.bttn6=tkinter.Button(self.mainFrame,text="6",width=3)
        self.bttn6.grid(row=4,column=2, padx=2,pady=2)
        
        self.bttnMult=tkinter.Button(self.mainFrame,text="X",width=3)
        self.bttnMult.grid(row=4,column=3, padx=2,pady=2)
        
        #==================Fila 3===================
        self.bttn1=tkinter.Button(self.mainFrame,text="1",width=3)
        self.bttn1.grid(row=5,column=0, padx=2,pady=2)
        
        self.bttn2=tkinter.Button(self.mainFrame,text="2",width=3)
        self.bttn2.grid(row=5,column=1, padx=2,pady=2)
        
        self.bttn3=tkinter.Button(self.mainFrame,text="3",width=3)
        self.bttn3.grid(row=5,column=2, padx=2,pady=2)
        
        self.bttnResta=tkinter.Button(self.mainFrame,text="-",width=3)
        self.bttnResta.grid(row=5,column=3, padx=2,pady=2)
        
        #==================Fila 4===================
        self.bttnDot=tkinter.Button(self.mainFrame,text=".",width=3)
        self.bttnDot.grid(row=6,column=0, padx=2,pady=2)
        
        self.bttn0=tkinter.Button(self.mainFrame,text="0",width=3)
        self.bttn0.grid(row=6,column=1, padx=2,pady=2)
        
        self.bttnIgual=tkinter.Button(self.mainFrame,text="=",width=3,height=3)
        self.bttnIgual.grid(row=6,column=2, padx=2,pady=2,rowspan=2)
        
        self.bttnSuma=tkinter.Button(self.mainFrame,text="+",width=3)
        self.bttnSuma.grid(row=6,column=3, padx=2,pady=2)
        
        #==================Fila 5===================
        self.bttnClean=tkinter.Button(self.mainFrame,text="C",width=3)
        self.bttnClean.grid(row=7,column=3, padx=2,pady=2)
        
        self.bttnejemplo=tkinter.Button(self.mainFrame,text="ejemplo",width=8)
        self.bttnejemplo.grid(row=7,column=0, padx=2, pady=2, columnspan=2)
        self.window.mainloop()
        
    # createWindow
    
    #Creamos la calculadora
if __name__ == '__main__':
    myCalc = Calc()
    myCalc.createWindow()
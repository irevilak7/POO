from tkinter import ttk
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
        #==================Renglon 1===================
        #self.texto1=tkinter.StringVar()
        self.combobox1=ttk.Combobox(self.mainFrame)
        self.combobox1.bind("<<ComboboxSelected>>", self.comboboxAction)
        self.combobox1.grid(row=0,column=0, padx=10,pady=10,columnspan=2)
        self.combobox1["values"] = ["Trimestral", "Semestral", "Anual"]
        bttnGraficar = tkinter.Button(self.mainFrame,text="Graficar",width=10, command=self.ejemploBoton)
        bttnGraficar.grid(row=0, column=3, padx=10,pady=10)
        #==================Renglon 2===================
        self.label1 = tkinter.Label(self.mainFrame,text="Primer mes")
        self.label1.grid(row=1, column=0, padx=10,pady=10)
        self.texto1=tkinter.StringVar()
        self.entrada1=tkinter.Entry(self.mainFrame, textvariable=self.texto1)
        self.entrada1.grid(row=1,column=1, padx=10,pady=5)
        
        self.label2 = tkinter.Label(self.mainFrame,text="Segundo mes")
        self.label2.grid(row=1, column=2, padx=10,pady=10)
        self.texto2=tkinter.StringVar()
        self.entrada2=tkinter.Entry(self.mainFrame, textvariable=self.texto2)
        self.entrada2.grid(row=1,column=3, padx=10,pady=10)
        
        #==================Renglon 3===================
        self.label3 = tkinter.Label(self.mainFrame,text="Tercer mes")
        self.label3.grid(row=2, column=0, padx=10,pady=10)
        self.texto3=tkinter.StringVar()
        self.entrada3=tkinter.Entry(self.mainFrame, textvariable=self.texto3)
        self.entrada3.grid(row=2,column=1, padx=10,pady=5)
        
        self.label4 = tkinter.Label(self.mainFrame,text="Cuarto mes")
        self.label4.grid(row=2, column=2, padx=10,pady=10)
        self.texto4=tkinter.StringVar()
        self.entrada4=tkinter.Entry(self.mainFrame, textvariable=self.texto4)
        self.entrada4.grid(row=2,column=3, padx=10,pady=10)
        
        #==================Renglon 4===================
        self.label5 = tkinter.Label(self.mainFrame,text="Quinto mes")
        self.label5.grid(row=3, column=0, padx=10,pady=10)
        self.texto5=tkinter.StringVar()
        self.entrada5=tkinter.Entry(self.mainFrame, textvariable=self.texto5)
        self.entrada5.grid(row=3,column=1, padx=10,pady=5)
        
        self.label6 = tkinter.Label(self.mainFrame,text="Sexto mes")
        self.label6.grid(row=3, column=2, padx=10,pady=10)
        self.texto6=tkinter.StringVar()
        self.entrada6=tkinter.Entry(self.mainFrame, textvariable=self.texto6)
        self.entrada6.grid(row=3,column=3, padx=10,pady=10)
        
        #==================Renglon 5===================
        self.label7 = tkinter.Label(self.mainFrame,text="Septimo mes")
        self.label7.grid(row=4, column=0, padx=10,pady=10)
        self.texto7=tkinter.StringVar()
        self.entrada7=tkinter.Entry(self.mainFrame, textvariable=self.texto7)
        self.entrada7.grid(row=4,column=1, padx=10,pady=5)
        
        self.label8 = tkinter.Label(self.mainFrame,text="Octavo mes")
        self.label8.grid(row=4, column=2, padx=10,pady=10)
        self.texto8=tkinter.StringVar()
        self.entrada8=tkinter.Entry(self.mainFrame, textvariable=self.texto8)
        self.entrada8.grid(row=4,column=3, padx=10,pady=10)
        
        #==================Renglon 6===================
        self.label9 = tkinter.Label(self.mainFrame,text="Noveno mes")
        self.label9.grid(row=5, column=0, padx=10,pady=10)
        self.texto9=tkinter.StringVar()
        self.entrada9=tkinter.Entry(self.mainFrame, textvariable=self.texto9)
        self.entrada9.grid(row=5,column=1, padx=10,pady=5)
        
        self.label10 = tkinter.Label(self.mainFrame,text="Decimo mes")
        self.label10.grid(row=5, column=2, padx=10,pady=10)
        self.texto10=tkinter.StringVar()
        self.entrada10=tkinter.Entry(self.mainFrame, textvariable=self.texto10)
        self.entrada10.grid(row=5,column=3, padx=10,pady=10)
        
        #==================Renglon 7===================
        self.label11 = tkinter.Label(self.mainFrame,text="Onceavo mes")
        self.label11.grid(row=6, column=0, padx=10,pady=10)
        self.texto11=tkinter.StringVar()
        self.entrada11=tkinter.Entry(self.mainFrame, textvariable=self.texto11)
        self.entrada11.grid(row=6,column=1, padx=10,pady=5)
        
        self.label12 = tkinter.Label(self.mainFrame,text="Doceavo mes")
        self.label12.grid(row=6, column=2, padx=10,pady=10)
        self.texto12=tkinter.StringVar()
        self.entrada12=tkinter.Entry(self.mainFrame, textvariable=self.texto12)
        self.entrada12.grid(row=6,column=3, padx=10,pady=10)
        
        self.window.mainloop()

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
        if (opcion=="Semestral"):
            print(2)
        if (opcion=="Anual"):
            print(3)
    def ejemploBoton(self, event=None):
            self.label4.lower(self.mainFrame)
            self.label5.lower(self.mainFrame)
            self.label6.lower(self.mainFrame)
            self.label7.lower(self.mainFrame)
            self.label8.lower(self.mainFrame)
            self.label9.lower(self.mainFrame)
            self.label10.lower(self.mainFrame)
            self.label11.lower(self.mainFrame)
            self.label12.lower(self.mainFrame)
        

    #Creamos la calculadora
if __name__ == '__main__':
    myCalc = Calc()
    myCalc.createWindow()
    
    
    
    
    
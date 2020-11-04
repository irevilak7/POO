
import tkinter

class Palindromo:
    
    def __init__(self):
        self.__aNumIdx = 1
        self.__aOper = ''
        
    def createWindow(self):
        self.window = tkinter.Tk()
        
        self.window.title("Palindromo")
        self.window.geometry("570x310+100+200")
        self.textOriginal = tkinter.StringVar()
        self.CadenaOriginal = tkinter.Entry(self.window, bg="lightgray", width=60, justify='right', textvariable=self.textOriginal)
        self.CadenaOriginal.place(x=10, y=10)
        self.textInvertida = tkinter.StringVar()
        self.CadenaInvertida = tkinter.Entry(self.window, bg="lightgray", width=60, justify='right', textvariable=self.textInvertida)
        self.CadenaInvertida.place(x=10, y=40)
        self.Comprobar = tkinter.Button(self.window, text = "Comprobar", command = self.Comprobar_click)
        self.Comprobar.place(x= 10, y=100, width=75)
        self.window.mainloop()
        
    def Comprobar_click(self):
        #textbox1 = self.CadenaOriginal.get()
        #textbox2 = textbox1[::-1]
        #self.CadenaInvertida.set(textbox2)
        self.textInvertida.set(self.textOriginal.get()[::-1])
        if self.textOriginal.get() == self.textInvertida.get():
            tkinter.messagebox.showerror("Correcto", "Si son iguales")
        else:
            tkinter.messagebox.showerror("Error", "No son iguales")
#if __name__ == '__main__':
myPali = Palindromo()
myPali.createWindow()



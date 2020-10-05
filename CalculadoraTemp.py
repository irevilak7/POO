
import tkinter

def prSetTxt(pTxt, pVal):
    pTxt.delete(0, len(pTxt.get()))
    pTxt.insert(0, pVal)
# prSetTxt

class Calc:
    
    def __init__(self):
	
		# Ingresar código
		
    # Constructor
    
    def createWindow(self):
        self.window = tkinter.Tk()
        
        self.window.title("Calc Win")
        self.window.geometry("385x310+100+200")
        
        self.txt01 = tkinter.Entry(self.window, bg="lightgray", width=60, justify='right')
        self.txt01.place(x=10, y=10)
        
		# Ingresar código
		
		self.btn07 = tkinter.Button(self.window, text = "7", command = self.btn07_click)
        self.btn07.place(x= 10, y=100, width=75)
       
        # Ingresar código
		
        self.window.mainloop()
    # createWindow

    def _btn(self, pVal):
        if (self.__aNumIdx == 1):
            lTxt = self.txt01
        else:
            lTxt = self.txt02
        lVal = lTxt.get() + pVal
        prSetTxt(lTxt, lVal)
    #_btn
    
    def _oper(self, pOper):
        if self.__aNumIdx == 1:
            if (self.txt01.get() == "") and (self.txt02.get() == "") and (self.txt03.get() != ""):
                prSetTxt(self.txt01, self.txt03.get())
                self.txt03.delete(0, len(self.txt03.get()))
                self.__aNumIdx = 2
            elif self.txt01.get() != "":
                self.__aNumIdx = 2
            self.__aOper = pOper
    # _oper

    def btn07_click(self):
        self._btn('7')
    # btn07_click
    
    # Ingresar código
	
    def btndiv_click(self):
        self._oper('/')
    # btndiv_click
    
    # Ingresar código
	
    def btndot_click(self):
	
		# Ingresar código
		
    # btndot_click
    
    # Ingresar código

    def btnequ_click(self):
	
		# Ingresar código
		
    # btnequ_click
    
    # Ingresar código
    
# Calc


if __name__ == '__main__':
    myCalc = Calc()
    myCalc.createWindow()

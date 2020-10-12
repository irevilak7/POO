import tkinter
import math
import os.path

def prSetTxt(pTxt, pVal):
    pTxt.delete(0, len(pTxt.get()))
    pTxt.insert(0, pVal)
# prSetTxt

class Calc:
    
    def __init__(self):
        self.__aNumIdx = 1
        self.__aOper = ''
    # Constructor
    
    def _log(self, pMssg):
        lFile = open("log.txt", "at")
        lFile.write(pMssg)
        lFile.close()
    # _log
    
    def _getLog(self):
        if os.path.isfile("log.txt"):
            lFile = open("log.txt", "rt")
            for lLine in lFile:
                self.txtLog.insert(tkinter.END, lLine)
            lFile.close()
    # _getLog
    
    def createWindow(self):
        self.window = tkinter.Tk()
        
        self.window.title("Calc Win")
        self.window.geometry("570x350+100+200")
        
        self.sbLog = tkinter.Scrollbar(self.window)
        self.sbLog.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        
        self.txtLog = tkinter.Text(self.window, bg="lightgray", width=20, height=20,
                                   wrap=tkinter.NONE, yscrollcommand=self.sbLog.set)
        self.txtLog.place(x=390, y=10)
        self.sbLog.config(command=self.txtLog.yview)
        
        self.txt01 = tkinter.Entry(self.window, bg="lightgray", width=60, justify='right')
        self.txt01.place(x=10, y=10)
       
        self.txt02 = tkinter.Entry(self.window, bg="lightgray", width=60, justify='right')
        self.txt02.place(x=10, y=40)
        
        self.txt03 = tkinter.Entry(self.window, bg="lightgray", width=60, justify='right')
        self.txt03.place(x=10, y=70)
        
        self.btn07 = tkinter.Button(self.window, text = "7", command = self.btn07_click)
        self.btn07.place(x= 10, y=100, width=75)
        
        self.btn08 = tkinter.Button(self.window, text = "8", command = self.btn08_click)
        self.btn08.place(x=105, y=100, width=75)
        
        self.btn09 = tkinter.Button(self.window, text = "9", command = self.btn09_click)
        self.btn09.place(x=200, y=100, width=75)
        
        self.btndiv = tkinter.Button(self.window, text = "/", command = self.btndiv_click)
        self.btndiv.place(x=295, y=100, width=75)
        
        self.btn04 = tkinter.Button(self.window, text = "4", command = self.btn04_click)
        self.btn04.place(x= 10, y=140, width=75)
        
        self.btn05 = tkinter.Button(self.window, text = "5", command = self.btn05_click)
        self.btn05.place(x=105, y=140, width=75)
        
        self.btn06 = tkinter.Button(self.window, text = "6", command = self.btn06_click)
        self.btn06.place(x=200, y=140, width=75)
        
        self.btntim = tkinter.Button(self.window, text = "*", command = self.btntim_click)
        self.btntim.place(x=295, y=140, width=75)
        
        self.btn01 = tkinter.Button(self.window, text = "1", command = self.btn01_click)
        self.btn01.place(x= 10, y=180, width=75)
        
        self.btn02 = tkinter.Button(self.window, text = "2", command = self.btn02_click)
        self.btn02.place(x=105, y=180, width=75)
        
        self.btn03 = tkinter.Button(self.window, text = "3", command = self.btn03_click)
        self.btn03.place(x=200, y=180, width=75)
        
        self.btnmin = tkinter.Button(self.window, text = "-", command = self.btnmin_click)
        self.btnmin.place(x=295, y=180, width=75)
        
        self.btndot = tkinter.Button(self.window, text = ".", command = self.btndot_click)
        self.btndot.place(x= 10, y=220, width=75)
        
        self.btn00 = tkinter.Button(self.window, text = "0", command = self.btn00_click)
        self.btn00.place(x=105, y=220, width=75)
        
        self.btnequ = tkinter.Button(self.window, text = "=", command = self.btnequ_click)
        self.btnequ.place(x=200, y=220, width=75)
        
        self.btnplu = tkinter.Button(self.window, text = "+", command = self.btnplu_click)
        self.btnplu.place(x=295, y=220, width=75)
        
        self.btncos = tkinter.Button(self.window, text = "cos", command = self.btncos_click)
        self.btncos.place(x=10, y=260, width=75)
        
        self.btncos = tkinter.Button(self.window, text = "sin", command = self.btnsin_click)
        self.btncos.place(x=105, y=260, width=75)
        
        self.btncos = tkinter.Button(self.window, text = "tan", command = self.btntan_click)
        self.btncos.place(x=200, y=260, width=75)
        
        self.btncan = tkinter.Button(self.window, text = "C", command = self.btncan_click)
        self.btncan.place(x=295, y=260, width=75)
        
        self.btncos = tkinter.Button(self.window, text = "pow", command = self.btnpow_click)
        self.btncos.place(x=10, y=300, width=75)
        
        self.btncan = tkinter.Button(self.window, text = "C Log", command = self.btnclg_click)
        self.btncan.place(x=295, y=300, width=75)
        
        self._getLog()
        
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
            else:
                tkinter.messagebox.showerror("Error", "Ingrese un # antes que un operador.")
            self.__aOper = pOper
    # _oper

    def btn07_click(self):
        self._btn('7')
    # btn07_click
    
    def btn08_click(self):
        self._btn('8')
    # btn08_click

    def btn09_click(self):
        self._btn('9')
    # btn09_click
    
    def btndiv_click(self):
        self._oper('/')
    # btndiv_click
    
    def btn04_click(self):
        self._btn('4')
    # btn04_click
    
    def btn05_click(self):
        self._btn('5')
    # btn05_click

    def btn06_click(self):
        self._btn('6')
    # btn06_click
    
    def btntim_click(self):
        self._oper('*')
    # btntim_click
    
    def btn01_click(self):
        self._btn('1')
    # btn01_click
    
    def btn02_click(self):
        self._btn('2')
    # btn02_click

    def btn03_click(self):
        self._btn('3')
    # btn03_click
    
    def btnmin_click(self):
        self._oper('-')
    # btnmin_click
    
    def btndot_click(self):
        if (self.__aNumIdx == 1):
            lTxt = str(self.txt01.get())
            if (lTxt.find('.') == -1):
                if (len(lTxt) == 0):
                    prSetTxt(self.txt01, '0.')
                else:
                    prSetTxt(self.txt01, lTxt + '.')
        else:
            lTxt = str(self.txt02.get())   
            if (lTxt.find('.') == -1):
                if (len(lTxt) == 0):
                    prSetTxt(self.txt02, '0.')
                else:
                    prSetTxt(self.txt02, lTxt + '.')
    # btndot_click
    
    def btn00_click(self):
        self._btn('0')
    # btn00_click

    def btnequ_click(self):
        if (self.__aNumIdx == 2):
            if (self.txt01.get() != "") and (self.txt02.get() != ""):
                lNum01 = float(self.txt01.get())
                lNum02 = 0.0
                if (self.txt02.get() != " "):
                    lNum02 = float(self.txt02.get())
                lNum03 = 0.0;
                if (self.__aOper == '+'):
                    lNum03 = lNum01 + lNum02
                elif (self.__aOper == '-'):
                    lNum03 = lNum01 - lNum02
                elif (self.__aOper == '*'):
                    lNum03 = lNum01 * lNum02
                elif (self.__aOper == '/'):
                    lNum03 = lNum01 / lNum02
                elif (self.__aOper == 'cos'):
                    lNum03 = math.cos(lNum01)
                elif (self.__aOper == 'sin'):
                    lNum03 = math.sin(lNum01)
                elif (self.__aOper == 'tan'):
                    lNum03 = math.tan(lNum01)
                elif (self.__aOper == 'pow'):
                    lNum03 = math.pow(lNum01, lNum02)
                    
                if (self.__aOper == 'cos') or (self.__aOper == 'sin') or (self.__aOper == 'tan'):
                    lMssg = self.__aOper + '( ' + str(lNum01) + ' ) = ' + str(lNum03) + "\n"
                elif (self.__aOper == 'pow'):
                    lMssg = str(lNum01) + ' ^ ' + str(lNum02) + ' = ' + str(lNum03) + "\n"
                else:   
                    lMssg = str(lNum01) + ' ' + self.__aOper + ' ' + str(lNum02) + ' = ' + str(lNum03) + "\n"
                self.txtLog.insert(tkinter.END, lMssg)
                self._log(lMssg)
                
                self.txt01.delete(0, len(self.txt01.get()))
                self.txt02.delete(0, len(self.txt02.get()))
                prSetTxt(self.txt03, str(lNum03))
            self.__aNumIdx = 1
    # btnequ_click
    
    def btnplu_click(self):
        self._oper('+')
    # btnplu_click
    
    def btncos_click(self):
        self._oper('cos')
        prSetTxt(self.txt02, " ")
        self.btnequ_click()
    #btncos_click
    
    def btnsin_click(self):
        self._oper('sin')
        prSetTxt(self.txt02, " ")
        self.btnequ_click()
    #btnsin_click
    
    def btntan_click(self):
        self._oper('tan')
        prSetTxt(self.txt02, " ")
        self.btnequ_click()
    #btntan_click
    
    def btnpow_click(self):
        self._oper('pow')
    #btnpow_click
    
    def btncan_click(self):
        self.txt01.delete(0, len(self.txt01.get()))
        self.txt02.delete(0, len(self.txt02.get()))
        self.txt03.delete(0, len(self.txt03.get()))
        self.__aNumIdx = 1
        self.__aOper = ''
    # btncan_click
    
    def btnclg_click(self):
        self.txt01.delete(0, len(self.txt01.get()))
        self.txt02.delete(0, len(self.txt02.get()))
        self.txt03.delete(0, len(self.txt03.get()))
        self.txtLog.delete('1.0', tkinter.END)
        self.__aNumIdx = 1
        self.__aOper = ''
        lFile = open("log.txt", "wt")
        lFile.close()
    # btnclg_click
    
# Calc


if __name__ == '__main__':
    myCalc = Calc()
    myCalc.createWindow()

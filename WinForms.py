
import tkinter

class Forms:
    
    def createWindow(self):
        self.window = tkinter.Tk()
        
        self.window.title("Demo Window")
        self.window.geometry("500x500+100+200")
        
        self.lbl01 = tkinter.Label(self.window, text="Hola Mundo!")
        self.lbl01.grid(column=0, row=0)
        
        self.btn01 = tkinter.Button(self.window, text="Enviar",
                                    command=self.btn01_click)
        self.btn01.grid(column=1, row=1)
        
        self.window.mainloop()
    # createWindow
    
    def btn01_click(self):
        tkinter.messagebox.showerror("Error", "Esto es una prueba")
        self.lbl01.configure(text="Se dió clic al botón")
    # btn01_click

# Forms
    
if __name__ == '__main__':
    myForm = Forms()
    myForm.createWindow()














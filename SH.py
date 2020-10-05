
class SH:
    
    def __init__(self, Fuer, Des, Cons, Int, Car):
        self.__Fuerza = Fuer
        self.__Destreza = Des
        self.Constitucion = Cons
        self.Inteligencia = Int
        self.Carisma = Car
    # Constructor
    
    @property
    def Fuerza(self):
        return self.__Fuerza
    # get Fuerza
    
    @Fuerza.setter
    def Fuerza(self, Fuer):
        if (0 <= Fuer) and (Fuer <= 100):
            self.__Fuerza = Fuer
    # set Fuerza
    
    @property
    def Destreza(self):
        return self.__Destreza
    # get Fuerza
    
    @Destreza.setter
    def Destreza(self, Des):
        if (0 <= Des) and (Des <= 100):
            self.__Destreza = Des
    # set Destreza
    
    def __repr__(self):
        return "F:{}, D:{}, O:{}, I:{}, C:{}".format(self.Fuerza,
                  self.Destreza, self.Constitucion,
                  self.Inteligencia, self.Carisma)
    # __repr__
    
    def DagnoRecibido(self, pVal):
        #       set = get
        self.Fuerza = self.Fuerza - int(0.3 * pVal)
        self.Constitucion -= int(0.7 * pVal)
    # DagnoRecibido

# SH

        
class Superman(SH):
    
    def __init__(self, pVul):
        super().__init__(100, 100, 100,  90, 100)
        self.Vul = pVul
    # Constructor
    
    def DagnoRecibido(self, pVal):
        #self.Fuerza -= int(0.3 * pVal)
        self.Constitucion -= pVal
    # DagnoRecibido
    
# Superman
    

class Batman(SH):
    
    def __init__(self, pVehi):
        super().__init__( 70,  90,  50, 100,  50)
        self.Vehi = pVehi
    # Constructor
    
# Batman


print("Superman")
SM = Superman("Kriptonita azul")
print(SM)
SM.DagnoRecibido(10)
print(SM)
SM.Fuerza = -13
print(SM)


print("Batman")
BM = Batman("Batimoto")
print(BM)
BM.DagnoRecibido(100)
print(BM)
BM.Fuerza = BM.Fuerza * 2
print(BM)
BM.Fuerza = 99
print(BM)
print(BM._SH__Fuerza)
BM._SH__Fuerza = 10000
print(BM)

#print(dir(BM))





    


















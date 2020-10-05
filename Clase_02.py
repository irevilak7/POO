
import random

class Tub:
    
    def __init__(self, Nom, Col, Nut, Agu):
        self.Nom = Nom
        self.Col = Col
        self.Nut = Nut
        self.Agu = Agu # % agura del tub
        
        self.Agua = 0 # ltr
        self.Inso = 0 # hrs
        self.Peso = 0 # gr
    # Constructor
    
    def __repr__(self):
        #return "{} de color: {}, con nutrientes: {} y {} % de agua".format(
        #        self.Nom, self.Col, self.Nut, self.Agu)
        return "Agua: {}, Insol: {} y Peso: {}".format(
                self.Agua, self.Inso, self.Peso)
    # __repr__
    
    def Crecer(self):
        pass
    # Crecer
    
    def DarleAgua(self, pAgua):
        self.Agua += pAgua
        self.Crecer()
    # DarleAgua
    
    def DarleSol(self, pInso):
        self.Inso += pInso
        self.Crecer()
    # DarleSol
    
# Tub


class Zanahoria(Tub):
    
    def __init__(self, Tam):
        super().__init__("Zanahoria", "Naranja", ['Vit A', 'Calcio', 'Vit C'],
             87)
        self.Tam = Tam
    # Constructor
    
    def __repr__(self):
        #return "{} de color: {}, con nutrientes: {} y {} % de agua y con tamaño: {} ".format(
        #        self.Nom, self.Col, self.Nut, self.Agu, self.Tam)
        return "Agua: {}, Insol: {} y Peso: {}".format(
                self.Agua, self.Inso, self.Peso)
    # __repr__
    
    def Crecer(self):
        lQAgua = self.Agua // 10
        lRAgua = self.Agua  % 10
        # 25 lt
        # lQAgua = 2
        # lRAgua = 5
        lQSol = self.Inso // 24
        lRSol = self.Inso  % 24
        # 32 hr
        # lQSol = 1
        # lRsol = 8
        
        if lQAgua > 0 and lQSol > 0:
            # 1 QA y 1 QS -> Crecer   X gr
            # 2 QA y 2 QS -> Crecer 2*X gr
            # 2 QA y 1 QS -> Crecer   X gr y me sobra 1 QA
            if lQAgua < lQSol:
                lRSol += (lQSol - lQAgua) * 24
                lQSol = lQAgua
            if lQAgua > lQSol:
                lRAgua += (lQAgua - lQSol) * 10
                lQAgua = lQSol
            
            self.Peso += 50 * lQAgua
            
            self.Agua = lRAgua
            self.Inso = lRSol
        # if
    #Crecer

# Zanahoria
    
Zan = Zanahoria("chico")
print(Zan)

Idx = 1
Salir = False
TAgua = 0
TSol = 0
while Salir == False:
    Ag = random.randint(0, 20)
    Zan.DarleAgua(Ag)
    TAgua += Ag
    So = random.randint(0, 20)
    Zan.DarleSol(So)
    TSol += So
    print(Zan)
    print("--{}--".format(Idx))
    Idx += 1
    if Zan.Peso >= 1000:
        Salir = True
# While

print("---")
print(Zan)
print(TAgua, TSol)














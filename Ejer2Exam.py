class Vegetal: #Crea la clase
    def __init__(self, variedad):
        self.Variedad = variedad
    def Alimentarse(self, x): #Describe 
        print("{} se alimenta {} horas de sol".format(self.Variedad, x))
        
class Animal: #Crea la clase
    def __init__(self, especie):
        self.Especie = especie
    def Alimentarse(self, x): #Describe
        print("{} se alimenta de {} entes".format(self.Especie, x))
    
class Zanahoria(Vegetal): #Hereda de la clase Vegetal
    def __init__(self, peso): #Define el peso de la Zanahoria
        self.Peso = peso
        super().__init__("Zanahoria") #Dice de que se esta hablando
    def Alimentarse(self, x):
        self.Peso = self.Peso + 10 * (x // 10)
    def __repr__(self):
        return"{} pesa {}g".format(self.Variedad, self.Peso)

class Conejo(Animal): #Heredan de la clase Animal
    def __init__(self, peso):
        self.Peso = peso
        super().__init__("Conejo")
    def Alimentarse(self, x): #Aumenta de peso dependiendo de la cantidad que coma
        self.Peso = self.Peso + x.Peso / 4
    def __repr__(self):
        return"{} pesa {}g".format(self.Especie, self.Peso)

zanahoria=Zanahoria(20)
conejo=Conejo(200)
print(conejo)
conejo.Alimentarse(zanahoria)
print(conejo)

class Zorro(Animal): #Hereda de la clase Animal
    def __init__(self, peso):
        self.Peso = peso
        super().__init__("Zorro")
    def Alimentarse(self, x): #Aumenta de peso dependiendo de la cantidad que coma
        self.Peso = self.Peso + x.Peso / 5 
    def __repr__(self):
        return"{} pesa {}g".format(self.Especie, self.Peso)
    def Hacerdelbano(self):
        self.Peso = self.Peso - 20

zorro=Zorro(1000)
print(zorro)
zorro.Alimentarse(conejo)
print(zorro)
zorro.Hacerdelbano()
print(zorro)
















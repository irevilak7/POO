
import random

class Ladrillo():
    
    def __init__(self):
        self.Peso = random.randint(3200, 4100) # gr
    # Constructor
    
# Ladrillo
    
class Ventana():
    
    def __init__(self):
        self.Peso = random.randint(20200, 40100) # gr
    # Constructor
    
# Ventana
    
# Puerta

# Techo

# Pintura

class Muro():

    def __init__(self):
        self.Ladrillos = []
        self.Ventanas = []
    # Constructor
    
    def Agrega(self, pLad):
        self.Ladrillos.append(pLad)
    # Agrega
    
    def AgregaV(self, pVent):
        self.Ventanas.append(pVent)
    # AgregaV
    
    def Peso(self):
        lPeso = 500 * len(self.Ladrillos)
        for lLad in self.Ladrillos:
            lPeso += lLad.Peso
        for lVen in self.Ventanas:
            lPeso += lVen.Peso
        return lPeso
    # Peso
    
    def NLadrillos(self):
        return len(self.Ladrillos)
    # NLadrillos
    
    def NVentanas(self):
        return len(self.Ventanas)
    # NVentanas

# Muro
    
# Ancho x Alto -> metros, Ladrillo mide (X, Y) metros
    
#   === === ===
#   = === === =
#   === === ===

# Casa


lLad = Ladrillo()
#print(lLad.Peso)

lMuro = Muro()
#print(lMuro.Peso())

lMuro.Agrega(lLad)
#print(lMuro.Peso())

lMuro.AgregaV(Ventana())
lMuro.AgregaV(Ventana())

while lMuro.Peso() < 1000000:
    lMuro.Agrega( Ladrillo() )

print(lMuro.Peso())
print(lMuro.NLadrillos())
print(lMuro.NVentanas())



















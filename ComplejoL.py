import math
class Complejo:
    def __init__(self, pReal=0, pImaginaria=0):
        self.Real = pReal
        self.Imaginaria = pImaginaria
        
    def __repr__(self):
        return "{}, {}i".format(self.Real, self.Imaginaria)
    
    def __add__(self, a):
        tReal = self.Real + a.Real
        tImaginaria = self.Imaginaria + a.Imaginaria
        return Complejo(tReal, tImaginaria)
    
    def __sub__(self, a):
        tReal = self.Real - a.Real
        tImaginaria = self.Imaginaria - a.Imaginaria
        return Complejo(tReal, tImaginaria)
    
    def __mul__(self, a):
        tReal = self.Real * a.Real - self.Imaginaria *a.Imaginaria
        tImaginaria = self.Imaginaria * a.Real + self.Real *a.Imaginaria
        return Complejo(tReal, tImaginaria)
    
    def Mag(self):
        return math.sqrt(self.Real*self.Real + self.Imaginaria*self.Imaginaria)
    
Complejo1 = Complejo(1,1)
print(Complejo1)
Complejo2 = Complejo(2, 5)
Suma = Complejo1 + Complejo2
print(Suma)
Resta = Complejo1 - Complejo2
print(Resta)
Multi = Complejo1 * Complejo2
print(Multi)
print(Complejo1.Mag())
print(Complejo1 + Complejo(1))








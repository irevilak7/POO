
class Gelatina:
    def __init__(self, sSabor):
        self.Sabor = sSabor
        self.Volumen = "1 L"
    def Mezclar(self):
        print("Se esta mezclando")
        print(self.Sabor)
    def Enfriar(self):
        print("Se esta enfriando")
        print(self.Sabor)
        
        
Gelatina1 = Gelatina("Fresa")
Gelatina2 = Gelatina("Limon")
Gelatina1.Mezclar()
Gelatina2.Mezclar()
print(Gelatina1.Volumen)
print(Gelatina2.Volumen)
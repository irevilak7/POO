
class Persona:
    
    def __init__(self, pNom, pApe):
        self.Nombre = pNom
        self.Apellido = pApe
    # Constructor
    
    def __repr__(self):
        return "Persona llamada: {} {}".format(self.Nombre, self.Apellido)
    # __repr__

# Persona
    
class Usuario(Persona):

    def __init__(self, pNom, pApe, pCorreo, pContra):
        #Persona.__init__(self, pNom, pApe)
        super().__init__(pNom, pApe)
        self.Correo = pCorreo
        self.Contra = pContra
    # __init__
    
    def __repr__(self):
        return "Persona llamada: {} {} ({}, {})".format(
                self.Nombre, self.Apellido, self.Correo, 
                '*' * len(self.Contra) )
    # __repr__
    
    def ValidaContra(self, pAProbar):
        return (self.Contra == pAProbar)
    # ValidaContra
    
# Usuario


Alguien = Persona("Clark", "Kent")
print(Alguien)

Usr = Usuario("Peter", "Parker", "spider@gmail.com", "1234")
print(Usr)

print("Dame la contrasegna: ")
Contra = input()

if Usr.ValidaContra(Contra) == True:
    print("Contrasegna correcta")
else:
    print("Contrasegna no valida")









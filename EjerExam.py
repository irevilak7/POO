class Minion:
    def __init__(self, nombre, ojos, estatura, cabello):
        self.Nombre = nombre
        self.Ojos = ojos
        self.Estatura = estatura
        self.Cabello = cabello
    def Soy(self):
        print("Soy el minion llamado {}, tengo {} ojos, mido {} y {} tengo pelo.".format(self.Nombre, 
                                                                                         self.Ojos,
                                                                                         self.Estatura, 
                                                                                         self.Cabello))
minion=Minion("David", 2, "60cm", "no")
minion.Soy()

class Bob(Minion):
    def __init__(self):
        super().__init__("Bob", 2, "30cm", "no")
    def Soy(self):
        print("Soy {}, tengo {} ojos, mido {}, {} tengo pelo y me gusta ayudar a Grub.".format(self.Nombre,
                                                                                               self.Ojos,
                                                                                               self.Estatura,
                                                                                               self.Cabello))
minion2=Bob()
minion2.Soy()

class Kevin(Minion):
    def __init__(self):
        super().__init__("Kevin", 2, "2 Metros", "si")
    def Soy(self):
        print("Soy {}, tengo {} ojos, mido {}, {} tengo pelo y me gusta jugar con Bob.".format(self.Nombre,
                                                                                               self.Ojos,
                                                                                               self.Estatura,
                                                                                               self.Cabello))
minion3=Kevin()
minion3.Soy()      

class Stuart(Minion):
    def __init__(self):
        super().__init__("Stuart", 1, "120cm", "si")
    def Soy(self):
        print("Soy {}, tengo {} ojo, mido {}, {} tengo pelo y me gusta jugar videojuegos.".format(self.Nombre,
                                                                                               self.Ojos,
                                                                                               self.Estatura,
                                                                                               self.Cabello))        
minion4=Stuart()
minion4.Soy()     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
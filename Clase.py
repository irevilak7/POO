
class Tabique:
    #Peso = 300
    
    def __init__(self, pPeso, pColor):
        self.Peso = pPeso
        self.Color = pColor
        self.Material = 'arcilla'
    # Constructor
    
    def Descr(self):
        print("Tabique de {} gramos y {} color.".format(self.Peso, self.Color))
    # Descr
    
# Tabique

MiTab = Tabique(250, 'rojo')
print(MiTab.Peso, MiTab.Color)
MiTab.Descr()

TabII = Tabique(275, 'gris')
TabII.Descr()

TabII.Peso = 350
TabII.Descr()

TabII.Densidad = 3
print(TabII.Densidad)
del TabII.Densidad
#print(TabII.Densidad)

#del TabII.Color
#TabII.Descr()

#del TabII
#TabII.Descr()















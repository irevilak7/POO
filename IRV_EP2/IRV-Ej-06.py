class IRV_CeldaSolar:
     def __init__(self, material, peso, temperatura):
        self.IRV_Material = material
        self.IRV_Peso = peso
        self.IRV_Temperatura = temperatura
     def IRV_Cargar(self, horas):
        print("La celda genera electricidad con {} horas de sol".format(horas))
     def __repr__(self):
        return"La celda esta hecha de {} con un peso de {}kg y una temperatura de {} grados".format(self.IRV_Material, self.IRV_Peso, self.IRV_Temperatura)




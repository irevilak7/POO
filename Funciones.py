
def imprimeNombre(nombre, apep, apem):
    print("El nombre es: ", nombre)
    
def imprimeNombre_(*nombre):
    print("El nombre es: ", nombre[0])

def imprimeNombre__(**param):
    print("El nombre es: ", param["nombrePropio"])
    
def saludo(mensaje = "Buenos días"):
    print(mensaje)
    

imprimeNombre("G", "B", "R")

imprimeNombre_("G", "B", "R", "asda", "asdasd")

imprimeNombre(apem = "R", apep = "B", nombre = "G")

imprimeNombre__(nombrePropio="Gerardo", ape="B", ape2="R", alias="asda", 
               alias2="asdasd")


saludo("Buenas tardes")
saludo()























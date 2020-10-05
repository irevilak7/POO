
A = 1

B = [1, 2, 3]

# K:V

Auto = {
    "marca": "Tesla",
    "modelo": "S",
    "año": 2020
}
print(Auto)

print(Auto["modelo"])

print(Auto.get("marca"))

Auto["modelo"] = "SE"
Auto["año"] = 2021
print(Auto)

for Item in Auto:
    print(Item, Auto[Item])

for Val in Auto.values():
    print(Val)

for Key, Val in Auto.items():
    print(Key, Val)

Auto["potencia"] = 1000

if "potencia" in Auto:
    print(Auto["potencia"])
    
Auto.pop("año")
print(Auto)


print("---")

AutoII = Auto.copy()
#AutoII = dict(Auto)
print(Auto)
print(AutoII)
AutoII["potencia"] = 900
print(Auto)
print(AutoII)

print("---")

Persona = {
    "nombre": "Juan",
    "fnac": "1980-01-15",
    "hijos": {
        "uno": "Paty",
        "dos": "Pepe",
        "tres": "Lalo"
    }
}
print(Persona)
print(Persona["hijos"]["uno"])

print("---")

Hijos = {
    "uno": "Paty",
    "dos": "Pepe",
    "tres": "Lalo"
}

Persona = {
    "nombre": "Juan",
    "fnac": "1980-01-15",
    "hijos": Hijos    
}

print(Persona)
print(Persona["hijos"]["uno"])

print("---")

Auto = dict(marca="Tesla", modelo="S", año=2020)
print(Auto)













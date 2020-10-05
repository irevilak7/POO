
Ropa = ('pantalón', 'blusa', 'playera')
print(Ropa)
print(Ropa[2])

print("\n-----\n")

Ropa_ = list(Ropa)      # Lista a partir de la tupla
Ropa_[1] = "suéter"     # Cambiar el valor de la celda 1
Ropa = tuple(Ropa_)     # Construir una tupla a partir de la lista
print(Ropa)
print(type(Ropa))
print(type(Ropa_))

print("\n-----\n")

Ropa_ = list(Ropa)       # Lista a partir de la tupla
Ropa_.append("camiseta") # Añadiendo valor
Ropa = tuple(Ropa_)      # Construir una tupla a partir de la lista
print(Ropa)







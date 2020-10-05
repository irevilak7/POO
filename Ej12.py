"""
12.- Dada una cadena cualquiera, 
determine el porcentaje de caracteres que son números.
"""

Cad = "a b 123 cd 4 5 6 ."
lCuantos=0
for c in Cad:
    print(c)
    if c.isdigit() == True:
        lCuantos += 1
# for
        
print(lCuantos / len (Cad) * 100, '%')
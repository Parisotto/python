# Usando a biblioteca Math

from math import hypot

catetoOposto = float(input("Cateto oposto: "))
catetoAdjacente = float(input("Cateto adjacente: "))
hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** 0.5

print(f"A hipotenusa mede {hipotenusa: .2f}")

hipo = hypot(catetoOposto, catetoAdjacente)
print((f"Usando hypot: {hipo: .0f}"))



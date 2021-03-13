cadena = "Geringoso"
cadenaAux = []
res = ""
vocales = ["a", "e", "i", "o", "u"]

for char in cadena:
    if char in vocales:
        cadenaAux.append(char + "p" + char)
    else:
        cadenaAux.append(char)

print(res.join(cadenaAux))
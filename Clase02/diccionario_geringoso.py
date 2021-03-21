def toGeringoso(lista):
    res = {}
    vocales = ["a", "e", "i", "o", "u"]

    for cadena in lista:
        cadenaAux = []
        for char in cadena:
            if char in vocales:
                cadenaAux.append(char + "p" + char)
            else:
                cadenaAux.append(char)
        res[cadena] = "".join(cadenaAux)

    return res


print(toGeringoso(['banana', 'manzana', 'mandarina']))

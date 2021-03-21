import csv


def leer_camion(file):
    camion = []
    with open(file) as f:
        next(f)
        rows = csv.reader(f)
        for row in rows:
            try:
                lote = {
                    "nombre": row[0],
                    "cajones": int(row[1]),
                    "precio": float(row[2])
                }
                camion.append(lote)
            except:
                print("se encontro un error")
    return camion


def leer_precio():
    res = {}
    with open("../Data/precios.csv") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                res[row[0]] = float(row[1])
            except:
                print("error al leer una linea, el programa continua...")
    return res


camion = leer_camion("../Data/camion.csv")
precios = leer_precio()

total = 0
for fruta in camion:
    ganancia = (precios[fruta["nombre"]] - fruta["precio"]) * fruta["cajones"]
    print("ganancia para ", fruta["nombre"], "es de $", ganancia)
    total += ganancia
print("ganancia total: $", total)

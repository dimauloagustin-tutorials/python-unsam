import csv
import sys

def costo_camion(file):
    costo_total = 0
    with open(file) as f:
        next(f)
        rows = csv.reader(f)
        for row in rows:
            try:
                costo_total = (costo_total + int(row[1]) * float(row[2]))
            except:
                print("se encontro un error")
    return costo_total


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
import csv

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
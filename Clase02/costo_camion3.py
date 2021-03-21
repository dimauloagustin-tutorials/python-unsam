def costo_camion(file):
    costo_total = 0
    with open(file, 'rt') as f:
            next(f)
            for line in f:
                try:
                    vals = line.split(",")
                    costo_total = (costo_total + int(vals[1]) * float(vals[2]))
                except:
                    print("se encontro un error")
    return costo_total
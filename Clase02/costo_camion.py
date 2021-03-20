costo_total = 0
with open('../Data/camion.csv', 'rt') as f:
        next(f)
        for line in f:
            vals = line.split(",")
            costo_total = (costo_total + int(vals[1]) * float(vals[2]))

print(costo_total)
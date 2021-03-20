def buscar_precio(name):
    found = False
    with open("../Data/precios.csv", 'rt') as f:
            next(f)
            for line in f:
                vals = line[:-1].split(",")
                if vals[0] == name:
                    print("El precio de un cajón de",name,"es:",vals[1])
                    found = True
    if(not found):
        print(name, "no figura en el listado de precios.")
    
frase = 'todos somos programadores'
palabras = frase.split(" ")
frase_t = []

for palabra in palabras:
    frase_t.append(palabra[:-2] + palabra[-2:].replace("o", "e"))

print(" ".join(frase_t))
'todes somes programadores'

# Autor: Eduard Bolaños
def letrasUnicas(palabra):
    listaPalabras = list(palabra)
    lisSinRepetir = []

    for i in listaPalabras:
        if i not in lisSinRepetir:
            lisSinRepetir.append(i)

    print(lisSinRepetir)

letrasUnicas("hoola")

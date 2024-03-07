
# Autor: Eduard Bolaños
def devolver_distintos(num1,num2,num3):

    suma = num1+num2+num3

    numeroMaximo = max(num1,num2,num3)
    numeroMinimo = min(num1,num2,num3)
    numeroMedio = suma-(numeroMaximo + numeroMinimo)

    if suma > 15:
        print("El número maximo es:", numeroMaximo)
    if suma < 10:
        print("El número minimo es:", numeroMinimo)
    if suma >= 10 and suma <= 15:
        print("El número del medio es:", numeroMedio)

devolver_distintos(10, 1, 2)
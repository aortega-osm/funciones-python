#Ejercicio realizado por mi
def multiplicar_valores(*lista):
    resulta=1
    for numero in lista:
        resulta *= numero
        return resulta
print(multiplicar_valores(2, 3, 4, 9))


#Ejercicio realizado solucion
def MultiplicacionValores(*args):
    Resultado=1
    for numero in args:
        Resultado *= numero
    return Resultado
print(MultiplicacionValores(3,4,6,7))




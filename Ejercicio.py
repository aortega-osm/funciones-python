#Crear una funcion para sumar los valores recibidos de
# tipo numerico,utilizando argumentos variables +args como parametros
#de la funcion y regresar como resultado la suma de todos los valores
#pasados como argumentos.

def listavalores(*args):
    resultado=0
    for valor in args:
        resultado += valor
    return resultado

print(listavalores(3, 5, 6, 8, 9))

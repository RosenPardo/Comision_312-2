# Crear una función que reciba como parámetro un vector de números enteros. La función debe mostrar los números negativos de forma decreciente y luego los positivos de forma creciente. 
#Nota: solo se puede usar un vector, y se debe utilizar la menor cantidad de estructuras repetitivas.

from Ordenamiento_1 import *

def mostrar_lista(lista):
    for i in range(len(lista)):
        print(lista[i], end= " ")



def ordenar_vectores_signo(lista) -> list:

    lista_positivos = []
    lista_negativos = []

    for i in range(len(lista)):
        if lista[i] > 0:
            lista_positivos += [lista[i]]
        else:
            lista_negativos += [lista[i]]

    ordenar_array(lista_positivos)
    ordenar_array(lista_negativos, True)
    
    lista = lista_positivos + lista_negativos

    return lista



lista_test = [4, 1, -3, 5, -24, -1, 23, -5, 2]

mostrar_lista(lista_test)
print()

lista_ordenada = ordenar_vectores_signo(lista_test)

mostrar_lista(lista_ordenada)

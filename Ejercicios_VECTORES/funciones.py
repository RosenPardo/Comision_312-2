def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    """Funcion para inicializar una matriz.

    Args:
        cantidad_filas (int): Cantidad de índices en el array principal. 
        cantidad_columnas (int): Cantidad de índices en los arrays internos.
        valor_inicial (any): Valor con el que se rellenan los arrays.

    Returns:
        list: Matriz creada.
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas  
        matriz += [fila]
    return matriz

def cargar_lista(lista:list, mensaje_dato:str = "Ingrese el str a cargar: ") -> None:
    """
    Carga de valores a una lista inicializada de forma aleatoria, indicando el valor a incorporar y su ubicación en la lista

    Args:
        Lista (list): Lista a cargar
    """
    seguir = "s"
    for i in range(len(lista)):
        if lista[i] == 0:
            dato= input(mensaje_dato)
            lista[i] = dato

            if i == len(lista) - 1:
                break
            else:
                seguir = input("¿Desea seguir cargando? s/n: ")

                if seguir != "s":
                    print("No hay más espacios para cargar datos")
                    break

    return lista


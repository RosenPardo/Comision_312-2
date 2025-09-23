

# Array - arreglo - lista simple - vector
mi_vector = [1, 5, 6, 4]
#Para acceder al 5:
mi_vector[1] #5

#array - arreglo - lista compuesta - matriz
mi_matriz = [[2, 4, 5, 8], [6, 3, 1, 9]]
#para acceder al 2:

mi_matriz[0][0] #2
mi_matriz[0][1] #4
mi_matriz[0][2] #5



#Cómo recorrerla?:

for i in range(len(mi_matriz)): # 0 1
    for j in range(len(mi_matriz[i])): #i = 0 entonces j = 0, 1, 2, 3 cuando i = 1 entonces j = 0, 1, 2, 3
        print(mi_matriz[i][j], end= " ")
    print("")

print("\n")
#otra forma de imprimir:

for i in range(len(mi_matriz)): # 0 1
    for j in range(len(mi_matriz[i])):
        if len(mi_matriz)-1 == i and len(mi_matriz[i])-1 == j:
            print(mi_matriz[i][j])
        else:
            print(mi_matriz[i][j], end = " | ")


#Print con cambio de signos: https://onlinegdb.com/bsSRAnkOm

print("\n")
#Cómo crear e inicializar una matriz en Python:

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas  

        matriz += [fila]

    return matriz

mi_matriz = inicializar_matriz(2, 4, 0)

print(mi_matriz)

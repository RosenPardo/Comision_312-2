
'''
vectores:
estados
nombre
legajo
de 100 elementos

matriz de 100 por 3 elementos de números enteros, que van a representar las notas del curso de ingreso
ademas tendremos un vector de 100 elementos donde se cargaran los promedios de las tres notas

1 vector de estados (0/1)
1 vector de nombres
1 vector de legajo (puede ser secuencial, al indice 0 le pongo 0, al indice 1 le pongo legajo 1)
1 vector más del tipo float, para calcular el promedio

Hacer 1 menú de opciones donde:
1= Generar e inicializar los vectores y la matriz
2= Para cargar los datos (nombre, porque el legajo lo puedo sacar del índice)
3= Cargar notas en matiz
4= Calcular y poblar (asignar a cada elemento del vector) los promedios
5= Buscar por promedio >= que el dato a buscar y mostrar el listado de estudiantes que cumplan esa condición
6= Salir

Armar biblioteca "Ejercicio". Que cada opción de menú, sea un función y modularizar. 


son 4 vectores y 1 matriz. cada indice corresponde a 1 estudiante

Tienen que ser todas listas paralelas. 
'''

programa_activo = True

while programa_activo == True:
    try: 
        print(f"Lista estudiantes: {lista_estudiantes}")
        print(f"Lista estado legajos: {estado_legajo})")
    except:
        print("")
    menu = int(input("\n*MENÚ DE OPCIONES* " \
    "\n 1) Generar listado de estudiantes. \n " \
    "2) Carga de legajos. \n " \
    "3) Carga de notas. \n " \
    "4) Calcular promedios. \n " \
    "5) Buscar promedio. \n " \
    "6) Salir. \n " \
    "Seleccione el valor: "))

    match menu:
        case 1:
            print("GENERAR LISTADO DE ESTUDIANTES \n")
            
            cantidad_filas = int(input("Ingrese la cantidad de estudiantes: "))
            cantidad_columnas = int(input("Ingrese la cantidad de notas a cargar: ")) + 1
            
            def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
                matriz = []
                for i in range(cantidad_filas):
                    fila = [valor_inicial] * cantidad_columnas  
                    matriz += [fila]
                
                return matriz
            
            lista_estudiantes = inicializar_matriz(cantidad_filas, cantidad_columnas, 0)
            estado_legajo = inicializar_matriz(cantidad_filas, 1, 0)
        case 2:
            print("CARGA DE LEGAJOS \n")

            def cargar_nombre_legajo(matriz: list):
                """
                Carga de valores a una matriz inicializada de forma aleatoria, indicando el valor a incorporar y su ubicación en la matriz (fila y columna)

                Args:
                    matriz (list): Matriz a cargar
                """
                seguir = "s"
                while seguir == "s":
                    fila= int(input("Indique legajo de estudiante a cargar: "))
                    if estado_legajo[fila][0] == 0:
                        dato= input("Ingrese el nombre del estudiante: ")
                        matriz[fila][0] = dato
                        estado_legajo[fila][0] = 1
                    else:
                        print(f"El legajo {fila} se encuentra ocupado con el nombre {matriz[fila][0]}. ")
                    seguir = input("Desea seguir cargando nombres de legajos? s|n: ")
            cargar_nombre_legajo(lista_estudiantes)
        case 3 :
            def cargar_notas_legajo(matriz: list):
                    seguir = "s"
                    while seguir == "s":
                        fila= int(input("Indique legajo de estudiante: "))
                        if estado_legajo[fila][0] == 0:
                            print("El legajo se encuentra vacío. ")
                        else:
                            dato = input(f"Ingrese la nota a cargar en el legajo de {matriz[fila][0]}: ")
                            for i in range(len(matriz[fila])):
                                if matriz[fila][i] == 0:
                                    matriz[fila][i] = dato
                                    break
                        seguir = input("Desea continuar en el menú 'carga de notas?' s|n: ")
            
            cargar_notas_legajo(lista_estudiantes)
        case 4:
            print("PROMEDIO DE ESTUDIANTES \n")

            fila = input("Ingrese el legajo del estudiante: ")
            def calcular_promedios(matriz: list):
                for i in range(len(matriz)):
                    for j in range(len(matriz[fila])):
                        pass
        case 5:
            print("5")
        case 6:
            programa_activo = False


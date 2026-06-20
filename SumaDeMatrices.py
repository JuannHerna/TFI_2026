"""
Suma de Matrices
Este ejercicio debe permitir cargar dos matrices y calcular la suma 
de ambas, mostrando el resultado como una matriz.
"""

def cargar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Ingrese el valor para la posición ({i}, {j}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sumar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = []
    for i in range(filas):
        fila_resultado = []
        for j in range(columnas):
            suma = matriz1[i][j] + matriz2[i][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)
    return resultado

def mostrar_matriz(matriz):
    for fila in matriz:
        print("\t".join(map(str, fila)))
        
def main():
    filas = int(input("Ingrese el número de filas para las matrices: "))
    columnas = int(input("Ingrese el número de columnas para las matrices: "))

    print("Cargando la primera matriz:")
    matriz1 = cargar_matriz(filas, columnas)

    print("Cargando la segunda matriz:")
    matriz2 = cargar_matriz(filas, columnas)

    resultado = sumar_matrices(matriz1, matriz2)

    print("La suma de las matrices es:")
    mostrar_matriz(resultado)
if __name__ == "__main__":    
    main()
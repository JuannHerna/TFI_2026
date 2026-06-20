//
//Suma de Matrices
//Este ejercicio debe permitir cargar dos matrices y calcular la suma 
//de ambas, mostrando el resultado como una matriz.


Algoritmo SumaDeMatrices
	
    Definir filas, columnas, i, j Como Entero
	
    Escribir "Ingrese el numero de filas para las matrices:"
    Leer filas
	
    Escribir "Ingrese el numero de columnas para las matrices:"
    Leer columnas
	
    Dimension matriz1[filas, columnas]
    Dimension matriz2[filas, columnas]
    Dimension resultado[filas, columnas]
	
    Escribir "Cargando la primera matriz:"
    Para i <- 0 Hasta filas - 1 Hacer
        Para j <- 0 Hasta columnas - 1 Hacer
            Escribir "Ingrese el valor para la posicion (", i, ", ", j, "):"
            Leer matriz1[i, j]
        FinPara
    FinPara
	
    Escribir "Cargando la segunda matriz:"
    Para i <- 0 Hasta filas - 1 Hacer
        Para j <- 0 Hasta columnas - 1 Hacer
            Escribir "Ingrese el valor para la posicion (", i, ", ", j, "):"
            Leer matriz2[i, j]
        FinPara
    FinPara
	
    Para i <- 0 Hasta filas - 1 Hacer
        Para j <- 0 Hasta columnas - 1 Hacer
            resultado[i, j] <- matriz1[i, j] + matriz2[i, j]
        FinPara
    FinPara
	
    Escribir "La suma de las matrices es:"
	
    Para i <- 0 Hasta filas - 1 Hacer
        Para j <- 0 Hasta columnas - 1 Hacer
            Escribir Sin Saltar resultado[i, j], " "
        FinPara
        Escribir ""
    FinPara
	
FinAlgoritmo
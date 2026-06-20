//
//Tabla de multiplicar
//Generar un programa que permita visualizar la tabla de multiplicar de 
//un número "n" (n X 20) . (Donde el usuario debe ingresar el valor n)
//

Algoritmo TablaDeMultiplicar
	
    Definir n, i, resultado Como Entero
	
    Escribir "Ingrese el número para generar su tabla de multiplicar:"
    Leer n
	
    Escribir "Tabla de multiplicar del ", n, ":"
	
    Para i <- 1 Hasta 20 Hacer
        resultado <- n * i
        Escribir n, " x ", i, " = ", resultado
    FinPara
	
FinAlgoritmo
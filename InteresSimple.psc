
//Inter�s
//Escribir un programa que solicite al usuario ingresar el capital  y el 
//tiempo, y luego, permita calcular el inter�s simple


Algoritmo InteresSimple
	
    Definir capital, tiempo, interes Como Real
    Definir tasa Como Real
	
    tasa <- 5
	
    Escribir "La tasa de interes anual es: ", tasa, "%"
	
    Escribir "Ingrese el capital:"
    Leer capital
	
    Escribir "Ingrese el tiempo (en a�os):"
    Leer tiempo
	
    interes <- capital * tasa * tiempo / 100
	
    Escribir "El interes simple es: ", interes
	
FinAlgoritmo
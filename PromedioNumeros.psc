//"""Promedio
//Este ejercicio debe permitir ingresar una cantidad finita (hasta 10) 
//de números y luego calcular el promedio. El programa debe 
//finalizar cuando el usuario ingrese un valor negativo, el mismo no 
//se debe incluir en el promedio"""


Algoritmo PromedioNumeros
	
    Definir suma, num, promedio Como Real
    Definir contador Como Entero
	
    suma <- 0
    contador <- 0
	cortar <- Verdadero
    Mientras cortar y contador < 10 Hacer
		
        Escribir "Ingrese un numero (negativo para finalizar):"
        Leer num
		
        Si num < 0 Entonces
            cortar <- Falso
		SiNo
			suma <- suma + num
			contador <- contador + 1
		FinSi
    FinMientras
	
    Si contador > 0 Entonces
        promedio <- suma / contador
        Escribir "El promedio de los numeros ingresados es: ", promedio
    Sino
        Escribir "No se ingresaron numeros validos."
    FinSi
	
FinAlgoritmo
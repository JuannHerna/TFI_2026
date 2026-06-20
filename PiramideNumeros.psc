//Pirámide
//Escribir un programa donde el usuario deba ingresar un número y 
//pueda generarse una pirámide de números naturales, con altura igual 
//al número ingresado. (Cada escalón de la pirámide se conforma de 
//números naturales, y en cada uno de ellos, se agrega un elemento)

Algoritmo PiramideNumeros
	
    Definir altura, i, j, k, numero Como Entero
	
    Escribir "Ingrese la altura de la pirámide:"
    Leer altura
	
    numero <- 1
	
    Para i <- 1 Hasta altura Hacer
		
        // Imprimir espacios para centrar
        Para k <- 1 Hasta altura - i Hacer
            Escribir Sin Saltar "  "
        FinPara
		
        // Imprimir números de la fila
        Para j <- 1 Hasta i Hacer
            Escribir Sin Saltar numero, " "
            numero <- numero + 1
        FinPara
		
        Escribir ""
		
    FinPara
	
FinAlgoritmo
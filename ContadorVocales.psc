//Contador De Vocales
//Este ejercicio debe solicitar al usuario quie ingrese una palabra o frase. Para que sea analizada
//	y retorne cuantas vocales (tanto mayusculas como minusculas) contiene, mostrando el resultado 
//	de la salida.
//



Funcion cantidad <- ContarVocales(frase)
	
    Definir cantidad, i Como Entero
    Definir letra Como Cadena
	
    cantidad <- 0
	
    Para i <- 1 Hasta Longitud(frase) Hacer
        letra <- Subcadena(frase, i, i)
		
        Si letra = "a" O letra = "e" O letra = "i" O letra = "o" O letra = "u" O letra = "A" O letra = "E" O letra = "I" O letra = "O" O letra = "U" Entonces
            cantidad <- cantidad + 1
        FinSi
    FinPara
	
FinFuncion

Proceso ContadorVocales
	
    Definir frase Como Cadena
    Definir cantidad_vocales Como Entero
	
    Escribir "...Contador de Vocales..."
    Escribir "Ingrese una palabra o frase:"
    Leer frase
	
    cantidad_vocales <- ContarVocales(frase)
	
    Escribir "La cantidad de vocales en la frase es: ", cantidad_vocales
	
FinProceso

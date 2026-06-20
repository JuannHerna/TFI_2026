// Invertir
//Este ejercicio debe solicitar al usuario que ingrese una cadena de 
//texto o frase, y que la muestre invertida.

Algoritmo InvertirCadena
	
    Definir cadena, cadenaInvertida Como Cadena
    Definir i Como Entero
	
    Escribir "Ingrese una cadena de texto o frase:"
    Leer cadena
	
    cadenaInvertida <- ""
	
    Para i <- Longitud(cadena) Hasta 1 Con Paso -1 Hacer
        cadenaInvertida <- cadenaInvertida + Subcadena(cadena, i, i)
    FinPara
	
    Escribir "Cadena invertida: ", cadenaInvertida
	
FinAlgoritmo
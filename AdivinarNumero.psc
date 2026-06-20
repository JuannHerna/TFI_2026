//Adivinar
//Generar un programa donde a partir de  un número aleatorio 
//entre 1 y 25, permita al usuario adivinarlo. Indicando, además, si 
//	el número en cada intento es cercano  está alejado o es correcto. 
//	(Usar la función Azar)


Algoritmo AdivinarNumero
	
    Definir numeroAleatorio, intento, intentos Como Entero
    Definir adivinado Como Logico
	
    numeroAleatorio <- Aleatorio(1,25)
	
    intentos <- 0
    adivinado <- Falso
	
    Escribir "¡Bienvenido al juego de adivinar el número!"
    Escribir "Estoy pensando en un número entre 1 y 25. ¿Puedes adivinarlo?"
	
    Mientras NO adivinado Hacer
		
        Escribir "Ingresa tu intento:"
        Leer intento
		
        intentos <- intentos + 1
		
        Si intento < numeroAleatorio Entonces
            Escribir "Tu número es demasiado bajo. Intenta de nuevo."
        Sino
            Si intento > numeroAleatorio Entonces
                Escribir "Tu número es demasiado alto. Intenta de nuevo."
            Sino
                adivinado <- Verdadero
                Escribir "¡Felicidades! Has adivinado el número ", numeroAleatorio, " en ", intentos, " intentos."
            FinSi
        FinSi
		
    FinMientras
	
FinAlgoritmo
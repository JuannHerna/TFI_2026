"""
Adivinar
Generar un programa donde a partir de  un número aleatorio 
entre 1 y 25, permita al usuario adivinarlo. Indicando, además, si 
el número en cada intento es cercano  está alejado o es correcto. 
(Usar la función Azar
"""

import random


def generar_numero_aleatorio():
    return random.randint(1, 25)



def main():
    numero_aleatorio = generar_numero_aleatorio()
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 25. ¿Puedes adivinarlo?")

    while not adivinado:
        try:
            intento = int(input("Ingresa tu intento: "))
            intentos += 1

            if intento < numero_aleatorio:
                print("Tu número es demasiado bajo. Intenta de nuevo.")
            elif intento > numero_aleatorio:
                print("Tu número es demasiado alto. Intenta de nuevo.")
            else:
                adivinado = True
                print(f"¡Felicidades! Has adivinado el número {numero_aleatorio} en {intentos} intentos.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
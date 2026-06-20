"""Contador De Vocales
Este ejercicio debe solicitar al usuario quie ingrese una palabra o frase. Para que sea analizada
y retorne cuantas vocales (tanto mayusculas como minusculas) contiene, mostrando el resultado 
de la salida.
"""

def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    contador = 0

    for letra in frase:
        if letra in vocales:
            contador += 1

    return contador

def main():
    print("...Contador de Vocales...")
    frase = input("Ingrese una palabra o frase: ")
    cantidad_vocales = contar_vocales(frase)
    print(f"La cantidad de vocales en la frase es: {cantidad_vocales}")



if __name__ == "__main__":
    main()  

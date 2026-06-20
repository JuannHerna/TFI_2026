"""Invertir
Este ejercicio debe solicitar al usuario que ingrese una cadena de 
texto o frase, y que la muestre invertida.
"""


def invertir_cadena(cadena):
    """Invierte la cadena de texto proporcionada."""
    return cadena[::-1]

def main():
    cadena = input("Ingrese una cadena de texto o frase: ")
    cadena_invertida = invertir_cadena(cadena)
    print("Cadena invertida:", cadena_invertida)
if __name__ == "__main__":
    main()
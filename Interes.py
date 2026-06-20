"""
Interés
Escribir un programa que solicite al usuario ingresar el capital  y el 
tiempo, y luego, permita calcular el interés simple
"""

def calcular_interes_simple(capital, tiempo, tasa_interes):
    interes = (capital * tiempo * tasa_interes) / 100
    return interes

def main():
    capital = float(input("Ingrese el capital: "))
    tiempo = float(input("Ingrese el tiempo (en años): "))
    tasa_interes = 5.0  # Tasa de interés fija del 5%

    interes = calcular_interes_simple(capital, tiempo, tasa_interes)
    print(f"El interés simple es: {interes:.2f}")

if __name__ == "__main__":
    main()
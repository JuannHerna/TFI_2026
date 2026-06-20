"""Promedio
Este ejercicio debe permitir ingresar una cantidad finita (hasta 10) 
de números y luego calcular el promedio. El programa debe 
finalizar cuando el usuario ingrese un valor negativo, el mismo no 
se debe incluir en el promedio"""

def main():
    numeros = 0
    contador = 0
    while contador < 10:
        numero = float(input("Ingrese un número (negativo para finalizar): "))
        if numero < 0:
            break
        numeros += numero
        contador += 1

    if contador > 0:
        promedio = numeros / contador
        print(f"El promedio de los números ingresados es: {promedio}")
    else:
        print("No se ingresaron números válidos.")

if __name__ == "__main__":
    main()
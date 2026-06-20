"""
Pirámide
Escribir un programa donde el usuario deba ingresar un número y 
pueda generarse una pirámide de números naturales, con altura igual 
al número ingresado. (Cada escalón de la pirámide se conforma de 
números naturales, y en cada uno de ellos, se agrega un elemento)
"""

def generar_piramide(altura):
    numero = 1

    # Calcula el número más grande para saber el ancho necesario
    max_numero = altura * (altura + 1) // 2
    ancho = len(str(max_numero)) + 1

    for i in range(1, altura + 1):
        espacios = " " * ((altura - i) * ancho // 2)
        print(espacios, end="")

        for j in range(i):
            print(f"{numero:{ancho}d}", end="")
            numero += 1

        print()

def main():
    altura = int(input("Ingrese la altura de la pirámide: "))
    generar_piramide(altura)

if __name__ == "__main__":
    main()
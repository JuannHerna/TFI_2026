"""
Tabla de multiplicar
Generar un programa que permita visualizar la tabla de multiplicar de 
un número “n” (n X 20) . (Donde el usuario debe ingresar el valor n)
"""
# Solicitar al usuario que ingrese el número para el cual se desea generar la tabla de multiplicar
n = int(input("Ingrese el número para generar su tabla de multiplicar: "))
# Generar la tabla de multiplicar desde 1 hasta 20
print(f"Tabla de multiplicar del {n}:")
for i in range(1, 21):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")


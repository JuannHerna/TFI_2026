"""
Triángulo
Escribir un programa que calcule el área de un triángulo dados su 
base y su altura. (Donde el usuario debe ingresar los datos)
"""

# Solicitar al usuario que ingrese la base y la altura del triángulo
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
# Calcular el área del triángulo utilizando la fórmula: Área = (base * altura) / 2
area = (base * altura) / 2
# Mostrar el resultado al usuario
print(f"El área del triángulo es: {area}")

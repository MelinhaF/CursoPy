"""
Calcular el mayor de dos números ingresados por teclado usando un operador
ternario
"""
num1_str = input("Ingrese el primer número: ")
num2_str = input("Ingrese el segundo número: ")

num1 = float(num1_str)
num2 = float(num2_str)

num_mayor = num1 if num1 > num2 else num2
print(num_mayor)
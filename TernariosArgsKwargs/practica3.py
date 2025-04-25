"""
Determinar si un número es par o impar
"""
num_str = input("Ingrese un número: ")
num = int(num_str)
print("Este número es par" if num % 2 == 0 else "Este número es impar")
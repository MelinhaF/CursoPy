"""
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
"""
num1_str = input("Ingrese el primer número: ")
num2_str = input("Ingrese el segundo número: ")
try:
    num1 = float(num1_str)
    num2 = float(num2_str)
    resultado = num1 / num2
    print(f"El resultado de la division es: {resultado}")
except ZeroDivisionError as e:
    print("Ha ocurrido un error, no se puede dividir por cero")
    print(f"Detalles del error: {e}")
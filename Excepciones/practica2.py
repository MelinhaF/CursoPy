"""
Escribe un programa que intente sumar un número y una cadena. Si se produce un error
de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
"""
num_str = input("Ingrese un número: ")
str = input("Ingrese una cadena: ")
try:
    num = float(num_str)
    suma = num + str
    print(f"El resultado de la suma es: {suma}")
except TypeError as e:
    print("Ha ocurrido un error, no se pueden sumar un numero y una cadena")
    print(f"Detalles del error: {e}")
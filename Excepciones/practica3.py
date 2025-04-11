"""
Escribe un programa que intente acceder a una clave que no existe en un
diccionario. Si se produce una excepción KeyError, captura la excepción y muestra
"""
mi_diccionario = {"nombre": "Adrian", "edad": 21, "pais": "Venezuela"}
clave1 = input("Ingrese la clave que desea buscar en el diccionario: ")

try:
    valor = mi_diccionario[clave1]
    print(f"El valor de la clave '{clave1}' es: {valor}")
except KeyError as e:
    print(f"Error: La clave '{clave1}' no existe en el diccionario.")
    print(f"Detalles del error: {e}")
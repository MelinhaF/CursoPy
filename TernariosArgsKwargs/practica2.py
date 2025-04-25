"""
Buscar una palabra en una lista ingresada por teclado usando args y un operador
ternario
"""
def buscar_palabra(*args):
    palabra = input("Ingrese la palabra que quiere buscar: ")
    return f"'{palabra}' {'Si existe' if palabra in args else 'Lo siento, esa palabra no se encuentra en la lista'}"

lista = input("Ingrese las palabras de su lista separadas por espacios: ").split()
print(buscar_palabra(*lista))
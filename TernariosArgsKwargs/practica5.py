"""
Imprimir un mensaje de error si no se pasan suficientes argumentos
"""
def calcular_prom(*args):
    try:
        return sum(args) / len(args)
    except ZeroDivisionError:
        return "Lo siento, debes ingresar al menos un número para poder calcular el promedio"
    
print(calcular_prom())
print(calcular_prom(9,6,4,55,27,1.5))
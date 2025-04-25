"""
Calcular el promedio de una lista de números usando args y un operador ternario
"""
def calcular_prom(*args):
    return sum(args) / len(args) if len(args) > 0 else 0

print(calcular_prom(9,6,4,55,27,1.5))
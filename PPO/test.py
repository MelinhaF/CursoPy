from cc import CuentaCorriente
from ca import CuentaAhorro

cuenta_corriente = CuentaCorriente("Pedro Jimenez", "1111111", "1990/05/22", 1000)
cuenta_ahorro = CuentaAhorro("Melinha Fernandez", "888888", "1996/05/24", 2000)

print("\n--- Pruebas Cuenta Corriente ---")
cuenta_corriente.extraer(200)
cuenta_corriente.extraer(600) 

print("\n--- Pruebas Cuenta Ahorro ---")
cuenta_ahorro.depositar(300)
cuenta_ahorro.extraer(100)
print(f"Tasa de interés: {cuenta_ahorro.tasa_interes}")
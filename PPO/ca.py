from cb import CuentaBancaria

class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._tasa_interes = 0.001  
    
    def _calcular_interes(self):
        interes = self._saldo * self._tasa_interes
        self._saldo += interes
        return interes
    
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            interes = self._calcular_interes()
            print(f"Depósito: {monto} | Interés aplicado: {interes}")
            print(f"Saldo actual: {self.obtener_saldo()}")
        else:
            print("El monto a depositar debe ser mayor a 0")
    
    def extraer(self, monto):
        if monto <= self.obtener_saldo():
            self._saldo -= monto
            interes = self._calcular_interes()
            print(f"Extracción: {monto} | Interés aplicado: {interes}")
            print(f"Saldo actual: {self.obtener_saldo()}")
        else:
            print("No posee saldo suficiente para esta operación")
    
    def obtener_saldo(self):
        interes = self._calcular_interes()
        print(f"Interés aplicado al consultar: {interes}")
        return self._saldo
    
    def tasa_interes(self):
        return self._tasa_interes
        
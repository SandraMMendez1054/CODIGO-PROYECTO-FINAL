import re

# Clase para representar una cuenta bancaria
class CuentaBancaria:
    def __init__(self, nombre_completo, numero_cuenta, pin, saldo=1000):
        self.nombre_completo = nombre_completo
        self.numero_cuenta = numero_cuenta
        self.pin = pin
        self.saldo = saldo
        self.historial = []

    def consultar_saldo(self):
        self.historial.append("Consulta de saldo")
        return self.saldo

    def depositar(self, monto):
        self.saldo += monto
        self.historial.append(f"Depósito: ${monto}")
        return self.saldo

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            self.historial.append(f"Retiro: ${monto}")
            return True
        else:
            self.historial.append(f"Intento de retiro fallido: ${monto}")
            return False

    def buscar_en_historial(self, palabra_clave):
        return [mov for mov in self.historial if palabra_clave.lower() in mov.lower()]

# Función para extraer apellido usando expresión regular
def extraer_apellido(nombre_completo):
    coincidencia = re.search(r'\b(\w+)$', nombre_completo)
    return coincidencia.group(1) if coincidencia else ""

# Función para validar credenciales
def validar_credenciales(cuenta, pin_ingresado):
    return cuenta.pin == pin_ingresado

# Base de datos simulada
usuarios = [
    CuentaBancaria("Sandra López", "123456", "7890"),
    CuentaBancaria("Carlos Méndez", "654321", "4321")
]

# Inicio del programa
print("Bienvenido al simulador de cajero automático")

nombre = input("Ingrese su nombre completo: ")
apellido = extraer_apellido(nombre)
print(f"Su apellido es: {apellido} y tiene {len(apellido)} letras.")

cuenta_encontrada = None
intentos = 0

while intentos < 3 and not cuenta_encontrada:
    cuenta_input = input("Ingrese su número de cuenta: ")
    pin_input = input("Ingrese su PIN: ")
    for usuario in usuarios:
        if usuario.numero_cuenta == cuenta_input and validar_credenciales(usuario, pin_input):
            cuenta_encontrada = usuario
            break
    if not cuenta_encontrada:
        print("Datos incorrectos. Intente nuevamente.")
        intentos += 1

if not cuenta_encontrada:
    print("Demasiados intentos fallidos. Programa finalizado.")
else:
    salir = False
    while not salir:
        print("\nMenú de opciones:")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Buscar en historial")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"Su saldo actual es: ${cuenta_encontrada.consultar_saldo()}")
        elif opcion == "2":
            monto = float(input("Ingrese el monto a depositar: "))
            nuevo_saldo = cuenta_encontrada.depositar(monto)
            print(f"Depósito exitoso. Nuevo saldo: ${nuevo_saldo}")
        elif opcion == "3":
            monto = float(input("Ingrese el monto a retirar: "))
            if cuenta_encontrada.retirar(monto):
                print(f"Retiro exitoso. Nuevo saldo: ${cuenta_encontrada.saldo}")
            else:
                print("Fondos insuficientes.")
        elif opcion == "4":
            palabra = input("Ingrese palabra clave para buscar en historial: ")
            resultados = cuenta_encontrada.buscar_en_historial(palabra)
            if resultados:
                print("Movimientos encontrados:")
                for mov in resultados:
                    print("-", mov)
            else:
                print("No se encontraron movimientos con esa palabra.")
        elif opcion == "5":
            print("Gracias por usar el cajero. ¡Hasta pronto!")
            salir = True
        else:
            print("Opción no válida. Intente de nuevo.")

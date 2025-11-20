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
        if monto <= 0:
            self.historial.append(f"Intento de depósito inválido: ${monto}")
            return None
        self.saldo += monto
        self.historial.append(f"Depósito: ${monto}")
        return self.saldo

    def retirar(self, monto):
        if monto <= 0:
            self.historial.append(f"Intento de retiro inválido: ${monto}")
            return False
        if monto <= self.saldo:
            self.saldo -= monto
            self.historial.append(f"Retiro: ${monto}")
            return True
        else:
            self.historial.append(f"Intento de retiro fallido: ${monto}")
            return False

    def buscar_en_historial(self, palabra_clave):
        return [mov for mov in self.historial if palabra_clave.lower() in mov.lower()]

# Función para extraer apellido con soporte para acentos y ñ
def extraer_apellido(nombre_completo):
    coincidencia = re.search(r'\b([\wáéíóúñÁÉÍÓÚÑ]+)$', nombre_completo)
    return coincidencia.group(1) if coincidencia else ""

# Función para validar credenciales
def autenticar_usuario(usuarios):
    intentos = 0
    while intentos < 3:
        cuenta_input = input("Ingrese su número de cuenta: ")
        pin_input = input("Ingrese su PIN: ")
        for usuario in usuarios:
            if usuario.numero_cuenta == cuenta_input and usuario.pin == pin_input:
                return usuario
        print("Datos incorrectos. Intente nuevamente.")
        intentos += 1
    return None

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

cuenta_encontrada = autenticar_usuario(usuarios)

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
            try:
                monto = float(input("Ingrese el monto a depositar: "))
                nuevo_saldo = cuenta_encontrada.depositar(monto)
                if nuevo_saldo is not None:
                    print(f"Depósito exitoso. Nuevo saldo: ${nuevo_saldo}")
                else:
                    print("Error: El monto debe ser mayor a cero.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")

        elif opcion == "3":
            try:
                monto = float(input("Ingrese el monto a retirar: "))
                if cuenta_encontrada.retirar(monto):
                    print(f"Retiro exitoso. Nuevo saldo: ${cuenta_encontrada.saldo}")
                else:
                    print("Retiro fallido. Verifique el monto o su saldo disponible.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")

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
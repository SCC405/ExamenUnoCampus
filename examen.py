# Examen Uno


def consulta(saldo):
    print(f"Su saldo es: {saldo}")


def depositar(saldo):
    depos = int(input("Inserte su deposito: "))
    saldo = saldo + depos
    print("Deposito exitoso")
    return saldo


def retirar(saldo):
    retiro = int(input("Cuanto desea retirar: "))
    if retiro > saldo:
        print("Saldo insuficiente, intente nuevamente")
    else:
        saldo = saldo - retiro
        print("Retiro exitoso")
    return saldo


saldo = 1000

while True:

    print("""
    Bienvenido a tu banco de confianza, que desea realizar:
    1. Consultar saldo
    2. Depositar dinero
    3. Retirar dinero
    4. Salir
    """)

    opcion = int(input("Digite una opcion: "))

    if opcion == 1:
        consulta(saldo)
    elif opcion == 2:
        saldo = depositar(saldo)
    elif opcion == 3:
        saldo = retirar(saldo)
    elif opcion == 4:
        break
    else:
        print("Error digite de nuevo")
        continue

    menu = int(input("Desea ver nuevamente el menu? (1: si, 2: no) "))
    if menu == 2:
        break

print("Gracias por usar nuestro banco")
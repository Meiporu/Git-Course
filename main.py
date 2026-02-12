
def menu():
    print("Selecciona una opción:")
    print("1. Suma")
    print("2. Resta")
    print("3. Salir")

def leerValor(msg):
    val = int(input(msg))
    return val


if __name__ == "__main__":
    exit = False
    v1, v2 = 0, 0
    while not exit:
        menu()
        opt = leerValor("Selecciona alguna de las opciones: ")
        match(opt):
            case 1:
                v1 = leerValor("Ingresa el primer valor: ")
                v2 = leerValor("Ingresa el segundo valor: ")
                print(f"La suma de {v1} y {v2} es {v1 + v2}")
            case 2:
                v1 = leerValor("Ingresa el primer valor: ")
                v2 = leerValor("Ingresa el segundo valor: ")
                print(f"La resta de {v1} y {v2} es {v1 - v2}")
            case 3:
                print("Saliendo de programa...")
                exit = True
            case _:
                print("Opción no válida, intenta de nuevo.")
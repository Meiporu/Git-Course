eleccion = -1

menu = """ 
    Menú:
    1. Sumar
    2. Restar
        """

while eleccion < 1 or eleccion > 2:

    print(menu)

    eleccion = int(input())

num1 = int(input("Insertar el primer número:"))
num2 = int(input("Insertar el segundo número:"))


match(eleccion): 
    case 1: 
        print("Resultado suma: ", num1 +  num2)
    case 2:
        print("Resultado resta: ", num1 -  num2)
    case _:
        pass 
def leer_numeros():
    num1 = int(input("Insertar el primer número:"))
    num2 = int(input("Insertar el segundo número:"))

    return num1, num2

def suma(): 
    num1, num2 = leer_numeros()

    print("Resultado suma: ", num1 +  num2)

def restar(): 
    num1, num2 = leer_numeros()

    print("Resultado resta: ", num1 -  num2)

def multiplicar(): 
    num1, num2 = leer_numeros()

    print("Resultado multiplicacion: ", num1 *  num2)

def dividir(): 
    num1, num2 = leer_numeros()

    if num2 == 0:
        print("No se puede dividir entre 0 jefe")
        return

    print("Resultado division: ", num1 / num2)

eleccion = -1

menu = """ 
    Menú:
    0. Salir del programa
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
        """

while eleccion != 0:

    print(menu)

    eleccion = int(input())

    match(eleccion): 
        case 1: 
            suma()
            
        case 2:
            restar()

        case 3:
            multiplicar()

        case 4: 
            dividir()

        case _:
            pass 


    
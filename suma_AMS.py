menu= """Menu de opciones  
    1. Suma 
    2. Resta
    3. Salir"""

op= int(input(menu))

while op < 1 or op > 3:
   
    
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))

    if op == 1:
        resultado = num1 + num2
        print("El resultado de la suma es: ", resultado)
    elif op == 2:
        resultado = num1 - num2
        print("El resultado de la resta es: ", resultado)
    elif op == 3:
        print("Saliendo...")
        exit()
    

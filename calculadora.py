menu= """Menu de opciones  
    1. Suma 
    2. Resta
    3. Multiplicacion 
    4. Division
    5. Salir\n"""

op = 1

while op > 1 or op < 5:
    op= int(input(menu))
    
    match op:
        case 1:
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            resultado = num1 + num2
            print("El resultado de la suma es: ", resultado)
            

        case 2:
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            resultado = num1 - num2
            print("El resultado de la resta es: ", resultado)
            
            
        case 3:
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            resultado = num1 * num2
            print("El resultado de la multiplicacion es: ", resultado)
            
        case 4:
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            if(num2 == 0):
                print("No se puede dividir por cero")
            else:
                resultado = num1 / num2
                print("El resultado de la division es: ", resultado)
            
        case 5:
            print("Saliendo...")
            exit()
        case _:
            print("Opcion no valida, intente de nuevo")
   
            
    


    

print("Saliendo...")
   
    

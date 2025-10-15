#calculadora con python
bandera=True
while bandera:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    opcion=int(input("Elige una opcion: "))
    if opcion==1:
        num1=int(input("Dame el primer numero: "))
        num2=int(input("Dame el segundo numero: "))
        suma=num1+num2
        print("La suma es:", suma)
    elif opcion==2:
        num1=int(input("Dame el primer numero: "))
        num2=int(input("Dame el segundo numero: "))
        resta=num1-num2
        print("La resta es:", resta)
    elif opcion==3:
        num1=int(input("Dame el primer numero: "))
        num2=int(input("Dame el segundo numero: "))
        multiplicacion=num1*num2
        print("La multiplicacion es:", multiplicacion)
    elif opcion==4:
        num1=int(input("Dame el primer numero: "))
        num2=int(input("Dame el segundo numero: "))
        if num2!=0:
            division=num1/num2
            print("La division es:", division)
        else:
            print("No se puede dividir entre 0")
    elif opcion==5:
        bandera=False
    else:
        print("Opcion no valida")
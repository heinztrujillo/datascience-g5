#ENTRADA    
num1=int(input("Dame el primer numero: "))
num2=int(input("Dame el segundo numero: "))
operacion=input("Dame la operacion a realizar (suma, resta, multiplicacion, division): ")
#PROCESO
if operacion=="suma":
    resultado=num1+num2
elif operacion=="resta":
    resultado=num1-num2
#SALIDA
print("El resultado es:", {num1}, operacion, {num2}, "=", resultado)
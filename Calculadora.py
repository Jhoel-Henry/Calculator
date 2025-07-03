a = int(input("Digite el primer digito: "))
b= int(input("Digite el segundo digito "))
operacion = input("Ingrese que tipo de operacion quieres obtener: ")
if operacion == "+":
    print (a+b)
elif operacion =="-":
    print(a-b)
elif operacion == "*":
    print(a*b)
elif operacion == "/":
    print(a//b)
else:
    print ("La operacion no es valida, intentelo nuevamente")

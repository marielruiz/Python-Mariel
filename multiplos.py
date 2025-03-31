print("COMPARADOR DE MÚLTIPLOS")
num1=float(input("Escriba un número: "))
num2=float(input("Escriba otro número: "))
if(num1>num2):
    num3=num1/num2       
    if(float(num3).is_integer()):
     print(num1, " es múltiplo de ",num2)
    else:
     print(num1, " no es múltiplo de ",num2)
elif(num1<num2):
   num4=num2/num1
   if(float(num4).is_integer()):
     print(num2, " es múltiplo de ",num1)
   else:
     print(num2, " no es múltiplo de ",num1)




    
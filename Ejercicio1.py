print("COMPARADOR DE AÑOS BISIESTOS")
año1=int(input("Escriba un año y le diré si es bisiesto: "))
año2=año1/4
if(float(año2%400==0) or ((año2%4==0)) and (año2%100!=0)):
    print("Es año bisisesto")
else:
    print("No es un año bisiesto")


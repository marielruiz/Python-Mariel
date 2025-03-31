print("COMPARADOR DE AÑOS")
año1=int(input("¿En qué año estamos? "))
año2=int(input("Escriba un año cualquiera "))
if(año1<año2):
    año3=año2-año1
    print("Para llegar al año ",año2, " faltan ", año3, " años")
elif(año1>año2):
    año4=año1-año2
    print("Desde el año ", año2," han pasado ", año4, " años")
else:
    print("¡Son el mismo año!")
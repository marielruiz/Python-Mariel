
entero=1 

z= "hello kitty"
x= "don ramon"

rojo= True
verde= False

frutas=["cereza", "sandia","fresa", "limon", "piña"]
detodo=["hola",3,4,"conejo"]

print(entero)
print(z)
print(x)

print(z+x)
print(verde) #el verde es un amigo falso
print(frutas)
print(frutas[2])

edad=int(input("Dame tu edad "))
if(edad>=18 and edad<60):
    print ("Ya saca tu INE")
elif(edad>=60):
    print("debes sacar la tarjeta del INAPAM")
else:
    print("¡Eres un niño aún!")

#actividades de informática
print("valores absolutos")
a=int(input("Dame un número para que te regrese su valor absoluto:"))
if (a<0):
    a=a*-1
    print("El valor absoluto es: ", a)
else:
    print("El valor absoluto es: ", a)

#1
dividendo=int(input("Escribe el número que será el dividendo:"))
divisor=int(input("Escriba el número que será el divisor: "))
resultado=dividendo/divisor
if (float(resultado).is_integer()):
    print("La división es exacta: ",resultado)
else:
 print("La división no es exacta: ",resultado)
 

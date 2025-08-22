#Números pares:Pedir un número y mostrar todos los números pares desde 1 hasta ese número.

#con for
num = int(input("Ingresa un numero:"))
for i in range( 1 , num + 1):
    if i % 2 == 0:
        print(i)

#con while
num = int(input("Ingrese un numero:"))
contador = 1
while contador <= num:
    if contador % 2 == 0:
        print(contador)
    contador+=1
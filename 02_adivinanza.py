# Adivina el número del 1 al 10
import random

print("¡ESTE JUEGO ES UNA ADIVINANZA!")
print("Escribe '0' para terminar el juego")

while True:  # bucle para reiniciar el juego automáticamente
        num_secreto = random.randint(1, 10)  
        intentos = 0
        print("\nSe ha generado un número nuevo entre 1 y 10")
        
        while True:
                intento = int(input("Ingrese un número del 1 al 10: "))
                
                if intento == 0:  # salir del juego
                        print("Gracias por participar. ¡Hasta la próxima!")
                        exit()  # rompe todo el programa
                        
                if intento < 1 or intento > 10:
                        print("Solo números del 1 al 10")
                        continue
                intentos += 1
                
                if intento < num_secreto:
                        print("Es mayor, sigue intentando")
                elif intento > num_secreto:
                        print("Es menor, sigue intentando")
                else:
                        print("¡Muy bien, acertaste! El número era:", num_secreto)
                        print("Te tomó", intentos, "intentos")
                        print("-"*30)
                        break  # vuelve a iniciar un nuevo juego

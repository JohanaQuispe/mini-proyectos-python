# Juego de adivinar si el numero es par o impar

import random

print("¡Bienvenido al juego de PAR o IMPAR!")
print("Escribe 'salir' para terminar el juego.")

while True:
    numero = random.randint(1, 20)
    eleccion = input(f"¿El número {numero} es PAR o IMPAR? ").lower()

    if eleccion == "salir":
        print("Gracias por jugar. ¡Hasta la próxima!")
        break

    if numero % 2 == 0 and eleccion == "par":
        print("Correcto, es PAR")
    elif numero % 2 != 0 and eleccion == "impar":
        print("Correcto, es IMPAR")
    else:
        print("Incorrecto, intenta de nuevo")

    print("-" * 30)

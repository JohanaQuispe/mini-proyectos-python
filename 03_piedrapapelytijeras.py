import random
opciones = ["piedra","papel","tijera"]

print("¡BIENVENIDO AL JUEGO PIEDRA, PAPEL Y TIJERA!")
print("Escribe 'salir' para terminar el juego.")

while True:
    opcion_random = random.choice(opciones)
    eleccion = input("Escriba su elección: ").lower() #El lower por si escriben 'PapEl'

    if eleccion == "salir": 
        print("Gracias por jugar. ¡Hasta la próxima!")
        break #Para dejar de jugar

    if eleccion not in opciones:
        print("Escribe correctamente (piedra - papel - tijera)")
        continue #Ignora el resto del codigo y vuelve al inicio del bucle

    if opcion_random == eleccion: 
        print("EMPATE")
    elif (opcion_random == "piedra" and eleccion == "papel") or \
        (opcion_random == "papel" and eleccion == "tijera") or \
        (opcion_random == "tijera" and eleccion == "piedra"):
        print("GANASTE!!!") 
    else:
        print("PERDISTE")

    print("El bot sacó:", opcion_random) #Con esta linea de codigo te dice la eleccion random
    print("-"*30)
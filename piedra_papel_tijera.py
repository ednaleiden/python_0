import random

print("PIEDRA , PAPEL O TIJERA")
opciones = ['piedra', 'papel', 'tijera']
print("Jugador escoge piedra papel o tijera")
opciones_jugador = input()

if opciones_jugador in opciones:
    opciones_maquina = random.choice(opciones)
    print(f"Tú elegiste: {opciones_jugador}")
    print(f"La máquina eligió: {opciones_maquina}")

    if opciones_jugador == opciones_maquina:
        print("empate")
    elif (opciones_jugador == 'piedra' and opciones_maquina == 'tijera') or \
        (opciones_jugador == 'papel' and opciones_maquina == 'piedra') or \
        (opciones_jugador == 'tijera' and opciones_maquina == 'papel'):
        print("ganaste")
    else:
        print("perdiste")

print("gracias por jugar")
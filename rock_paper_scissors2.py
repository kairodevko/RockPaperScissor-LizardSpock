import random 
# Opciones de ganar 
# A qué números le gana cada opción:
reglas_victoria = {
    1: [3, 4],  # Piedra (1) le gana a Tijeras (3) y Lagarto (4)
    2: [1, 5],  # Papel (2) le gana a Piedra (1) y Spock (5)
    3: [2, 4],  # Tijeras (3) le gana a Papel (2) y Lagarto (4)
    4: [5, 2],  # Lagarto (4) le gana a Spock (5) y Papel (2)
    5: [3, 1]   # Spock (5) le gana a Tijeras (3) y Piedra (1)
}
# Mientras el usuario no gane
notPlayerWin = True
# Opcion de la computadora
computer = random.randint(1, 5)

while notPlayerWin:
    # Interfaz gráfica de juego
    print('==============================================')
    print('========= ROCK | PAPER | SCISSORS ============')
    print(' [1] -> ✊\n [2] -> ✋\n [3] -> ✌️\n [4] -> 🦎\n [5] -> 🖖')
    player = int(input('Pick a number [ 1 - 5 ]:\n>> '))

    if player < 1 or player > 5:
        print('===== Opción inválida. =====')
        continue
    
    elif computer in reglas_victoria[player]:
        print(f"Tu escogiste: {player} vs CPU: {computer}\n¡Tú ganaste! :)") 
        notPlayerWin = False
    
    else:
        print(f"Tú escogiste: [{player}] vs CPU: [{computer}]\n¡CPU GANÓ!")
        notPlayerWin = True
    







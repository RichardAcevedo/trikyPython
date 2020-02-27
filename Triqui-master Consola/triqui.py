tablero = {
    'A1': ' ', 'A2': ' ', 'A3': ' ',
    'M1': ' ', 'M2': ' ', 'M3': ' ',
    'B1': ' ', 'B2': ' ', 'B3': ' '
}

j1 = input("Nombre de jugador 1: ") # Registro jugador 1
j2 = input("Npmbre de jugador 2: ") # Registro jugador 2
puntaje = 0 # Controla puntaje jugador 1
#puntaje2 = 0 # Controla puntaje jugador 2
jugador = 1   # Para inicializar jugador
mov_total = 0 # Para contar los movimientos 
finalizar = 0 # Para finalizar 


def validar():
    # Comprobar movimientos del jugador 1
    # Para horizontal (inicio)
    if tablero['A1'] == 'X' and tablero['A2'] == 'X' and tablero['A3'] == 'X':
        #puntaje+=1
        print(j1,'gana ! ')
        print('Puntos: ',puntaje+1)
        return 1
    if tablero['M1'] == 'X' and tablero['M2'] == 'X' and tablero['M3'] == 'X':
        #puntaje1=puntaje1+1
        print(j1,'gana !')
        print('Puntos: ',puntaje+1)
        return 1
    if tablero['B1'] == 'X' and tablero['B2'] == 'X' and tablero['B3'] == 'X':
        #puntaje1=puntaje1+1
        print(j1,'gana !')
        print('Puntos: ',puntaje+1)
        return 1
    # Para horizontal (fin)
    # Para diagonal (inicio)
    if tablero['A1'] == 'X' and tablero['M2'] == 'X' and tablero['B3'] == 'X':
        #puntaje1=puntaje1+1
        print(j1,'gana !')
        print('Puntos: ',puntaje+1)
        return 1
    # Para diagonal (fin)
    # Para vertical (inicio)
    if tablero['A1'] == 'X' and tablero['M1'] == 'X' and tablero['B1'] == 'X':
        #puntaje1=puntaje1+1
        print(j1,'gana !')
        print('Puntos: ',puntaje+1)
        return 1
    if tablero['A2'] == 'X' and tablero['M2'] == 'X' and tablero['B2'] == 'X':
        #puntaje1=puntaje1+1
        print(j1,'gana !')
        print('Puntos: ',puntaje+1)
        return 1
    if tablero['A3'] == 'X' and tablero['M3'] == 'X' and tablero['B3'] == 'X':
        #puntaje1=puntaje1+1
        print(j1,'gana !')
        print('Puntos: ',puntaje+1)
        return 1
    # Para vertical (fin)

    # Comprobando movimientos del jugador 2
    if tablero['A1'] == 'O' and tablero['A2'] == 'O' and tablero['A3'] == 'O':
        #puntaje2=puntaje2+1
        print(j2,'gana !')
        print('Puntos: ',puntaje+1)
        return 1  # Se usa para finalizar el juego
    if tablero['M1'] == 'O' and tablero['M2'] == 'O' and tablero['M3'] == 'O':
        #puntaje2=puntaje2+1
        print(j2,'gana !')
        print('Puntos: ',puntaje+1)
        return 1
    if tablero['B1'] == 'O' and tablero['B2'] == 'O' and tablero['B3'] == 'O':
        #puntaje2=puntaje2+1
        print(j2,'gana !')
        print('Puntos: ',puntaje+1)
        return 1
    if tablero['A1'] == 'O' and tablero['M2'] == 'O' and tablero['B3'] == 'O':
        #puntaje2=puntaje2+1
        print(j2,'gana !')
        print('Puntos: ',puntaje+1)
        return 1
    if tablero['A1'] == 'O' and tablero['M1'] == 'O' and tablero['B1'] == 'O':
        #puntaje2=puntaje2+1
        print(j2,'gana !')
        print('Puntos: ',puntaje+1)
        return 1
    if tablero['A2'] == 'O' and tablero['M2'] == 'O' and tablero['B2'] == 'O':
        #puntaje2=puntaje2+1
        print(j2,'gana !')
        print('Puntos: ',puntaje+1)
        return 1
    if tablero['A3'] == 'O' and tablero['M3'] == 'O' and tablero['B3'] == 'O':
        #puntaje2=puntaje2+1
        print(j2,'gana !')
        print('Puntos: ',puntaje+1)
        return 1
    return 0


print('A1|A2|A3')
print('- +- +-')
print('M1|M2|M3')
print('- +- +-')
print('B1|B2|B3')
print('***************************')

while True:
    print(tablero['A1']+'|'+tablero['A2']+'|'+tablero['A3'])
    print('-+-+-')
    print(tablero['M1'] + '|' + tablero['M2'] + '|' + tablero['M3'])
    print('-+-+-')
    print(tablero['B1'] + '|' + tablero['B2'] + '|' + tablero['B3'])
    finalizar = validar()
    if mov_total == 9 or finalizar == 1:
        break
    while True:     # Entrada para jugadores
        if jugador == 1:  # Seleccion de jugador 1
            p1_input = input(j1+': ')
            if p1_input.upper() in tablero and tablero[p1_input.upper()] == ' ':
                tablero[p1_input.upper()] = 'X'
                jugador = 2
                break
            # Si la seleccion del recuadro es incorrecta
            else:
                print('Recuadro no existente, intentelo de nuevo')
                continue
        else: # Seleccion de jugador 2
            p2_input = input(j2+": ")
            if p2_input.upper() in tablero and tablero[p2_input.upper()] == ' ':
                tablero[p2_input.upper()] = 'O'
                jugador = 1
                break
            else:  # Si la seleccion del recuadro es incorrecta
                print('Recuadro no existente, intentelo de nuevo')
                continue
    mov_total += 1
    print('***************************')
    print()




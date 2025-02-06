'''
Este archivo es el punto de entrada de la aplicación. 
Aquí se importan las funciones de tablero.py y se ejecutan en un ciclo while.
'''
import tablero

def main():
    '''Función principal'''
    X = {"G":0, "P":0, "E":0}
    O = {"G":0, "P":0, "E":0}
    score = {"X":X, "O":O}
    numeros = [str(i) for i in range(1,10)]
    corriendo = True
    while corriendo:
        dsimbolos = {x:x for x in numeros}
        g = tablero.juego(dsimbolos)
        if g is not None:
            print(f'Ganador: {g}')
            if g == "X":
                X["X"]["G"] += 1
                O["O"]["P"] += 1
            elif g == "O":
                X["O"]["G"] += 1
                O["X"]["P"] += 1
            else:
                X["X"]["E"] += 1
                O["O"]["E"] += 1
        else:
            print("Empate")
            X["X"]["E"] += 1
            O["O"]["E"] += 1
                     
if __name__ == '__main__':
    main()
'''
Archivo principal del juego Game
'''
from Athlete import Athlete
from Team import Team
from Game import Game
from Sport import Sport
import json

def main(archivo_torneo:str):
    ''' Función principal del juego '''
    if archivo_torneo != "":
        with open(archivo_torneo, 'r') as file:
            torneo = json.load(file)
    else:
        players_mexico = ['Chicharito','Piojo','Chucky','Tecatito','Guardado','Ochoa','Herrera','Layun','Moreno','Araujo','Gallardo']
        players_espania = ['Ramos','Iniesta','Pique','Casillas','Xavi','Torres','Villa','Silva','Busquets','Alba','Alonso']
        players_brasil = ['Neymar','Ronaldo','Rivaldo','Kaka','Cafu','Roberto Carlos','Lucio','Ronaldinho','Romario','Bebeto','Taffarel']
        players_argentina = ['Messi','Maradona','Batistuta','Aguero','Di Maria','Mascherano','Zanetti','Crespo','Tevez','Veron','Ortega']
        lista_mexico = [Athlete(x) for x in players_mexico]
        lista_espania = [Athlete(x) for x in players_espania]
        lista_brasil = [Athlete(x) for x in players_brasil]
        lista_argentina = [Athlete(x) for x in players_argentina]
        soccer = Sport("Soccer", 11, "FIFA")
        mexico = Team("Mexico", soccer, lista_mexico)
        espania = Team("España", soccer, lista_espania)
        brasil = Team("Brasil", soccer, lista_brasil)
        argentina = Team("Argentina", soccer, lista_argentina)
        equipos = [mexico, espania, brasil, argentina]
        d = {}
        for local in equipos:
            for visitante in equipos:
                if local != visitante:
                    juego = Game(local, visitante)
                    d[juego.to_json()['A']['name']] = juego.to_json()       
                     
        juego = Game(mexico, espania)
        torneo = [juego.to_json()]
        archivo_torneo = "torneo.json"
        with open(archivo_torneo, "w",encoding= 'utf8') as f:
            json.dump(torneo, f, ensure_ascii=False, indent=4)
        print(f"Se escribio el archivo {archivo_torneo} con un torneo de {len(torneo)} juego(s)")
    # Jugar todos los juegos del torneo
    for juego in torneo:
        A = Team(juego['A']['name'], Sport(juego['A']['sport']['name'], juego['A']['sport']['players'], juego['A']['sport']['league']), [Athlete(x) for x in juego['A']['players']])
        B = Team(juego['B']['name'], Sport(juego['B']['sport']['name'], juego['B']['sport']['players'], juego['B']['sport']['league']), [Athlete(x) for x in juego['B']['players']])
        game = Game(A, B)
        game.play()
        print(game)
        print("-----------")
      
if __name__ == "__main__":
    archivo_torneo = "torneo.json"      
    main(archivo_torneo)  
        
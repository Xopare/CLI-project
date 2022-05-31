import os
import time
from UserTerm import GuionConsola
from UserTerm import GuionUsuario

GuionConsola = "..."
GuionUsuario = "/User: "
DefaultPythonCommand = "python "
DefaultPath = './Resources/Games/'

def Games():
    Gamelist = os.listdir(".\Resources\Games")
    Gamelist = list(map(lambda game: game.replace(".py",""),Gamelist))

    for game in Gamelist:
        print(Gamelist.index(game) + 1, game , "-",f"A fun recreation of {game} in Python!")
    
    while True:
        Gametoplay = str(input("Escribe el nombre o numero de juego que quieres jugar: "))
        if  Gametoplay.isnumeric() == False and Gametoplay in Gamelist:
            os.system(f"{DefaultPythonCommand}{DefaultPath}{Gametoplay}.py")
        elif Gametoplay == '--kill' or Gametoplay == '-k':
            break
        elif Gametoplay.isnumeric():
            os.system(f"{DefaultPythonCommand}{DefaultPath}{Gamelist[int(Gametoplay) -1]}.py")
        else:
            print("El juego Insertado no existe")

if __name__ == '__main__':
    Games()
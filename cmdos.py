import os 
from UserTerm import GuionConsola
from UserTerm import GuionUsuario

def wincommandline():
    commandline = input(f'{GuionConsola}Inserte el Comando para WINDOWS: ')
    os.system(commandline)
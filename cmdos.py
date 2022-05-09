import os 

GuionConsola = '/Term: '
GuionUsuario = '/User: '

def wincommandline():
    commandline = input(f'{GuionConsola}Inserte el Comando para WINDOWS: ')
    os.system(commandline)
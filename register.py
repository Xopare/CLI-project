from UserTerm import GuionConsola
from UserTerm import GuionUsuario
from UserTerm import DefaultDataFilename

file = open(DefaultDataFilename,"a")


def register():
    username = input(f'{GuionConsola}Antes de empezar a  usar la consola primero defina un nombre de usuario: ')
    password = input(f'{GuionConsola}Tambien necesitara una password: ').encode('utf-32')
    user = {'USERNAME': username,'PASSWORD': password}
    file.write(f"{user}\n")

if __name__ == '__main__':
    register()
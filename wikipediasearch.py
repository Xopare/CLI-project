import wikipedia

GuionConsola = '/Term: '
GuionUsuario = '/User: '

def wikipediasearch():
    search = input(f'{GuionConsola}Inserte Algo para Buscar: ')
    print(wikipedia.summary(search))

if  __name__ == '__main__':
    wikipediasearch()
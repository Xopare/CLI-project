import wikipedia

GuionConsola = '/Term: '
GuionUsuario = '/User: '

def wikipediasearch():
    search = input(f'{GuionConsola}Inserte Algo para Buscar: ')
    try:
        print(wikipedia.summary(search))
    except:
	    pass

if  __name__ == '__main__':
    wikipediasearch()
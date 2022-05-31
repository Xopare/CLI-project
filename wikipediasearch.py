from UserTerm import GuionConsola
from UserTerm import GuionUsuario
import wikipedia


def wikipediasearch(*args):
    search = args
    if search == "" or search == " ":
        search = input(f'{GuionConsola}Inserte Algo para Buscar: ')
    else:
        pass
    try:
        print(wikipedia.summary(search))
    except:
	    pass

if  __name__ == '__main__':
    wikipediasearch()
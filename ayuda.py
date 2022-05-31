from UserTerm import GuionConsola
from UserTerm import GuionUsuario
from UserTerm import Functions

def ayuda():
    for value , key in Functions.items():
        print(f"{key[0]} o {key[1]} // para {value}")

if __name__ == '__main__':
    ayuda()
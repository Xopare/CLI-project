from UserTerm import GuionConsola
from UserTerm import GuionUsuario
from UserTerm import UserIsLogged
import time
import register
import login
import wikipediasearch
import os
import cmdos 
import Boot
import ayuda
import Games

Boot.Boot()
IsUserLogged = UserIsLogged
errores= 0
nombre_proyecto = "CLI-Proyecto"
version = "Alpha 1.2"
hora = time.strftime('%I:%M %p', time.localtime())
fecha = time.strftime('del %d/%m/%y', time.localtime())
saludo = """
iniciado con {errores} errores!
Bienvenido a {nombre_proyecto} version {version}!
Por Co1dtuna / Stockastic

La hora es {hora}, {fecha}

inserte un comando para iniciar: 
""".format(errores=errores,nombre_proyecto=nombre_proyecto,version=version,hora=hora,fecha=fecha)
forbiddenCommands = ['time()','wikipedia()','IsUserLogged = True','cmd()']

def clear():
    os.system('cls')

def inicio():
    print(saludo)

def kill():
    print('Chau!')
    time.sleep(1)
    quit()

def login1():
    if login.registered_user == True:
        login.login()
        global IsUserLogged
        IsUserLogged = True
        global GuionUsuario
        GuionUsuario=f'/{login.Username}: '
        print(f'has entrado exitosamente {GuionUsuario}')
    else:
        register.register()

def register1():
    register.register()

def printtime():
    print('La hora es {hora1}, {fecha1}'.format(hora1 = time.strftime('%I:%M %p', time.localtime()), fecha1 = time.strftime('del %d/%m/%y', time.localtime())))

def wikipediasearch1(*args):
    wikipediasearch.wikipediasearch(args)

def cmd():
    cmdos.wincommandline()

def ayuda1():
    ayuda.ayuda()

def Games1():
    Games.Games()

if __name__ == '__main__':
    inicio()
    while True:
        command = input(GuionUsuario).split(" ")
        try:
            if command[0] not in forbiddenCommands:
                exec(command[0])
            else:
                print(f"{GuionConsola} Smart Ass!")
        except:
            if command[0] == '--help' or command[0] == '-h':
                ayuda1()
            elif command[0] == '--kill' or command[0] == '-k':
                kill()
            elif command[0] == '--login' or command[0] == '-l':
                login1()
            elif command[0] == '--register' or command[0] == '-r':
                register1()
            elif (command[0] == '--time' or command[0] == '-t') and IsUserLogged == True:
                printtime()
            elif (command[0] == '--wikipedia' or command[0] == '-w') and IsUserLogged == True:
                wikipediasearch1(command[1])
            elif command[0] == '--clear' or command[0] == '-cl':
                clear()
            elif command[0] == '--inicio' or command[0] == '-i':
                inicio()
            elif (command[0] == '--cmd' or command[0] == '-c') and IsUserLogged == True:
                cmd()
            elif (command[0] == '--games' or command[0] == '-g') and IsUserLogged == True:
                Games1()
            else:
                print(time.strftime('[%I:%M:%S]'),GuionConsola,'El comando no existe o no tienes acceso a el')
                
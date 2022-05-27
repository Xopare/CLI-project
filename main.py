import time
import register
import login
import wikipediasearch
import os
import cmdos 
import Boot
import ayuda
from rich import print as print

Boot.Boot()
IsUserLogged = False
GuionConsola = '/term: '
GuionUsuario = '/User: '
errores= 0
nombre_proyecto = "CLI-Proyecto"
version = "Alpha 1.0.2"
hora = time.strftime('%I:%M %p', time.localtime())
fecha = time.strftime('del %d/%m/%y', time.localtime())
saludo = """
iniciado con {errores} errores!
Bienvenido a {nombre_proyecto} version {version}!
Por Co1dtuna / Stockastic

La hora es {hora}, {fecha}

inserte un comando para iniciar: 
""".format(errores=errores,nombre_proyecto=nombre_proyecto,version=version,hora=hora,fecha=fecha)

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

def wikipediasearch1():
    wikipediasearch.wikipediasearch()

def cmd():
    cmdos.wincommandline()

def ayuda1():
    ayuda.ayuda()

if __name__ == '__main__':
    inicio()
    while True:
        command = input(GuionUsuario).replace(" ","")
        try:
            exec(command)
        except:
            if command == '--help':
                ayuda1()
            elif command == '--kill':
                kill()
            elif command == '--login':
                login1()
            elif command == '--register':
                register1()
            elif command == '--time' and IsUserLogged == True:
                printtime()
            elif command == '--wikipedia' and IsUserLogged == True:
                wikipediasearch1()
            elif command == '--clear':
                clear()
            elif command == '--inicio':
                inicio()
            elif command == '--cmd' and IsUserLogged == True:
                cmd()
            else:
                print(GuionConsola,'El comando no existe o no tienes acceso a el')
         
import time
import register
import login
import wikipediasearch
import os
import cmdos 

GuionConsola = '/Term: '
GuionUsuario = '/User: '
errores= 0
nombre_proyecto = "CLI-Proyecto"
version = "Alpha 1.0.1"
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

if __name__ == '__main__':
    inicio()
    while True:
        command = input(GuionUsuario)
        if command == '--help':
            pass
        elif command == '--kill':
            kill()
        elif command == '--login':
             login1()
        elif command == '--register':
            register1()
        elif command == '--time':
             printtime()
        elif command == '--wikipedia':
            wikipediasearch1()
        elif command == '--clear':
            clear()
        elif command == '--inicio':
            inicio()
        elif command == '--cmd':
            cmd()
        else:
            print(GuionConsola,'El comando no existe o no tienes acceso a el')
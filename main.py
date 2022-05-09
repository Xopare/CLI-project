import time
import register
import login
from colorama import Fore

GuionConsola = '/Term: ' + Fore.GREEN
GuionUsuario = '/User: ' + Fore.BLUE
errores= 0
nombre_proyecto = "CLI-Proyecto"
version = "Alpha 1.0.1"
hora = time.strftime('%I:%M %p', time.gmtime())
fecha = time.strftime('del %d/%m/%y', time.gmtime())
saludo = """
iniciado con {errores} errores!
Bienvenido a {nombre_proyecto} version {version}!
Por Co1dtuna / Stockastic

La hora es {hora}, {fecha}

inserte un comando para iniciar: 
""".format(errores=errores,nombre_proyecto=nombre_proyecto,version=version,hora=hora,fecha=fecha)

def inicio():
    print(saludo)
def kill():
    print('Chau!')
    quit()
def login_register():
    if login.registered_user == True:
        login.login()
    else:
        register.register()

if __name__ == '__main__':
    inicio()
    while True:
        command = input(GuionUsuario)
        if command == '--help':
            pass
        elif command == '--kill':
            kill()
        elif command == '--login':
             login_register()
        else:
            print(GuionConsola,'El comando no existe')
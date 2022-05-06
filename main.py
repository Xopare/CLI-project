import sys

# Cli principal - Aplicacion en plano

#Argumentos 

ArgumentoAyudaPrefijo = 'help'
ComandoKillProcess = 'end'
ListaArgumentos = [ArgumentoAyudaPrefijo, ComandoKillProcess]


#Tengo que ponerle un buen nombre al proyecto
NombreProyecto = "CLI-ForLife"
Version = "Alpha 1.0.0"
Saludo = """
Iniciado Correctamente errores 0

Bienvenido a {Nombre_Proyecto} version {Version_}!
Escribe {Argumento_Ayuda_Prefijo} para obtener ayuda
""".format(Nombre_Proyecto = NombreProyecto, Version_ = Version,Argumento_Ayuda_Prefijo = ArgumentoAyudaPrefijo)
MensajeHelp = """
Este es un proyecto creado para manejar parte mi vida digital y real a traves de una CLI modular con base python.

Los comandos disponibles son:

{Lista_Argumentos}

""".format(Lista_Argumentos =ListaArgumentos )

def main():
    print(Saludo)
    while True:
        UsrInput = input("Inserta un comando: ")
        if UsrInput == ArgumentoAyudaPrefijo:
            print(MensajeHelp)
        elif UsrInput == ComandoKillProcess:
            print('Chau!')
            quit()
        else:
            print("El Comando llamado no existe")

if __name__ == '__main__':
    main()

funcdict = {'--help':'Comando de ayuda','--kill':'Terminar la ejecucion del programa','--login':'Entrar al sistema','--register':'Registrarse en el sistema','--time':'Muestra la hora y la fecha','--wikipedia':'Busca un articulo en wikipedia','--inicio':'Muestra el inicio del sistema','--cmd':'Abre una instancia de cmd'}

def ayuda():
    for key in funcdict:
        print(key," : ",funcdict[key])

if __name__ == '__main__':
    ayuda()
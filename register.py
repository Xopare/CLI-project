from pip import main

file = open('usr_data.dat',"r+")

def register():
    username = input('Antes de empezar a  usar la consola primero defina un nombre de usuario: ')
    password = input('Tambien necesitara una password: ').encode('utf-32')
    user = {'USERNAME': username,'PASSWORD': password}
    file.write(f"{user}\n")

if __name__ == '__main__':
    register()
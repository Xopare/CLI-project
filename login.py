
from urllib.parse import uses_relative

GuionConsola = '/Term: '
GuionUsuario = '/User: '

file = open('usr_data.dat','r+')

user_data_list = file.read()

if user_data_list == '':
    registered_user = False
    pass
else:
    user_data_list =  user_data_list.splitlines()
    registered_user = True


def login(): 
     UserIsLogged = False
     while UserIsLogged == False:
         try_user = input(f'{GuionConsola}Escriba su usuario: ')
         try_pwd = input(f'{GuionConsola}Escriba su password: ').encode('utf-32')
         try_dict = {'USERNAME': try_user , 'PASSWORD': try_pwd}
         try_dict =str(try_dict)
         for i in user_data_list:
             if i == try_dict:
                 UserIsLogged = True
             else:
                 UserIsLogged
                 print(f'{GuionConsola}Usuario Incorrecto')

if __name__ == '__main__':
    login()

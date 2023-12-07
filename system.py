from library.interface import *
from library.arquive import *
from time import sleep

arq = 'database.txt'

if not arquiveExist(arq):
    createArquive(arq)

header('DATABASE SYSTEM v1.0')
while True:
    answer = menu(['See Registered People', 'Register People', 'Exit System'])
    if answer == 1:
        # This option list all the data registered in the database! #
        readArquive(arq)
    elif answer == 2:
        # This option registers a new person in the database! #
        header('NEW REGISTER')
        name = str(input('Name: '))
        age = readInt('Age: ')
        register(arq, name, age)
    elif answer == 3:
        # This option leaves the system! #
        header('Leaving the system... See you soon!')
        break
    else:
        # If a wrong option was typed in the menu! #
        print('\033[31mError! Please type an valid option!\033[m')
    sleep(2)

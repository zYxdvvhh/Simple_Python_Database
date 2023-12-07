from library.interface import *
def arquiveExist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createArquive(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('There was an error while creating the database!')
    else:
        print(f'The database {name} was successfully created!')


def readArquive(name):
    try:
        a = open(name, 'rt')
    except:
        print('There was an error while reading the database!')
    else:
        header('REGISTERED DATA')
        for line in a:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>3} years.')
    finally:
        a.close()


def register(arq, name='unknow', age=0):
    try:
        a = open(arq, 'at')
    except:
        print('There was an error while opening the database!')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('There was an error while writing the data!')
        else:
            print(f'{name} was successfully registered!')
            a.close()


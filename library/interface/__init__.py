def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mError! Please, type an valid number!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mData entry interrupted by the user!\033[m')
            return 0
        else:
            return n


def line(tam=42):
    return '-' * tam


def header(txt):
    print(line())
    print(txt.center(42))
    print(line())


def menu(list):
    header('MAIN MENU')
    c = 1
    for item in list:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(line())
    opc = readInt('\033[32mYour option: \033[m')
    return opc



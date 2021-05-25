def palindromo(string):
    try:
        if len(string) == 0:
            raise ValueError('No se puede ingresar un string vacio')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

def challenge(number):
    try:
        if number >= 0:
            print(number)
        else:
            raise ValueError('Es un número negativo')
    except ValueError as ve:
        print(ve)

if __name__ == '__main__':
    # string = input('Introduce un string: ')
    # try:
    #     print(palindromo(string))
    # except TypeError:
    #     print('No es un string')

    numero = int(input('Introduce un número: '))
    try:
        challenge(numero)
    except:
        print('Algo fallo')
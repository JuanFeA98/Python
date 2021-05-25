def palindromo(string):
    try:
        if len(string) == 0:
            raise ValueError('No se puede ingresar un string vacio')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

if __name__ == '__main__':
    string = input('Introduce un string: ')
    
    try:
        print(palindromo(string))
    except TypeError:
        print('No es un string')
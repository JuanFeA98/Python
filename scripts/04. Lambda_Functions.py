palindromo = lambda string: string == string[::-1]


if __name__ == '__main__':
    while True:
        palabra = input('Introduce la cadena de caracteres: ')
        if palabra != 'Exit':
            if palindromo(palabra):
                print('Es un palindromo')
            else:
                print('No es un palindromo')
        else:
            break
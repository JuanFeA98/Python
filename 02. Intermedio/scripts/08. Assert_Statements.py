def palindromo(string):
    assert len(string) > 0, 'No se puede ingresar una cadena vacía.'
    return string == string[::-1]

def number(num):
    assert num.isnumeric(), 'No es un número'
    print(num)

if __name__ == '__main__':
    # string = input('Introduce un string: ')
    numero = (input('Introduce un número: '))
    
    # print(palindromo(string))    
    number(numero)
from my_solution import my_solution

if __name__ == '__main__':
    contador = 1
    while contador == 1:
        country = input('Introduce el país: ')
        try:
            my_solution(country)
            rta = input('Quieres pobar con otro?(Y/N)').upper()
            if rta == 'N':
                contador += 1
        except:
            print('Nombre de pais invalido')

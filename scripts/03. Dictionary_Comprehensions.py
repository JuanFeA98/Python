import numpy as np

def run():
    # Key: Valor por Valor en Iterable if Condicion
    my_dict = {i: i**3 for i in range(1, 101) if i%3 != 0}
    print(my_dict)

    challenge = {i: round(np.sqrt(i), 2) for i in range(1, 1001)}
    print(challenge)


if __name__ == '__main__':
    run()
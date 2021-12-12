def read():
    numbers = []

    with open('./files/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    
    print(numbers)

def write():
    names = ['Sandra', 'Mayra', 'Gloria', 'Martha', 'Camila', 'Juan']
    
    with open('./files/names.txt', 'w', encoding='utf-8') as f:
        for i in names:
            f.write(i)
            f.write('\n')

if __name__ == '__main__':
    # read()
    write()
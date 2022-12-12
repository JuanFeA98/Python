import matplotlib.pyplot as plt

x = ['A', 'B', 'C']
y = [10, 5, 12]

def generate_barchar(labels, values, title):
    fig, ax = plt.subplots()
    ax.bar(labels, values)

    plt.title(title)

    plt.show()

def generate_piechart(labels, values, title):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')

    plt.title(title)

    plt.show()


if __name__ == '__main__':
    generate_piechart(x, y, 'Gráfico de barras')
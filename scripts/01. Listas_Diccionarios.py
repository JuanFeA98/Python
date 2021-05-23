def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {
                "firstname": 'Sandra',
                "lastname": "Martínez"
                }
    
    super_list = [
        {"firstname": 'Sandra', "lastname": "Martínez"},
        {"firstname": 'Juan', "lastname": "Martínez"},
    ]

    super_dict = {
        "natural": [1,2,3,4,5],
        "float": [1.5, 3.5, 2.4, 5.3],
    }

    for key, values in super_dict.items():
        print(key, values)

    for i in super_list:
        print(i)

if __name__ == '__main__':
    run()
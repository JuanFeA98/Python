import pandas as pd

import charts 

def my_solution(country):

    df = pd.read_csv('world_population.csv', index_col=0)
    df.rename(columns={'Country/Territory': 'Country'}, inplace=True)

    df_work = df.query(f'Country == "{country}"')
    df_work.reset_index(inplace=True)

    labels = list(filter(lambda x:'Population' in x,df_work.columns))
    labels.pop()
    labels.reverse()

    values = [df_work[i][0] for i in labels]

    charts.generate_barchar(labels, values, 'Poblacion')
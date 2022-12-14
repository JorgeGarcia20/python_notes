import csv
import matplotlib.pyplot as plt

'''
Usando el archivo world_population csv, crear una funcion o funciones que permitan extraer
dado un pais su crecimiento poblacional.
Dentro del documento existen varias columnas que hacen referencia a su crecimiento poblacional 
de acuerdo a varios años.
'''

def csv_to_dict(path):
    data = []
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
    
        for row in reader:
            iterable = zip(header, row)
            data_dict = {k: v for k, v in iterable}
            data.append(data_dict)
        
        return data

def get_country_data(data, country):
    return list(filter(lambda item: item['Country/Territory'] == country, data))


def get_population_growth(country_data):
    population = {
        '2022': int(country_data[0]['2022 Population']),
        '2020': int(country_data[0]['2020 Population']),
        '2010': int(country_data[0]['2010 Population']),
        '2000': int(country_data[0]['2000 Population']),
        '1990': int(country_data[0]['1990 Population']),
        '1980': int(country_data[0]['1980 Population']),
        '1970': int(country_data[0]['1970 Population'])
    }
    return population


def generate_bar_chart(labels, values, country):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.title(f'{country} population growth')
    plt.show()

def execute_program(country):
    world_data = csv_to_dict('world_population.csv')
    country_data = get_country_data(world_data, country)
    population = get_population_growth(country_data)
    keys = population.keys()
    values = population.values()
    generate_bar_chart(keys, values, country)

if __name__ == '__main__':
    country = input('Enter a contry to chart his population growth => ')
    execute_program(country.title())
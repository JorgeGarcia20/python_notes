import csv

def read_csv(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader) # list column names 
        data = []

        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
            return data


if __name__ == '__main__':
    result = read_csv('./world_population.csv')
    print(result[0])

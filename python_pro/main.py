import Operations

print(Operations.utils.sum_numbers(20, 20))
print(Operations.utils.multiplicate_numbers(20, 30))
print(Operations.utils.substract_numbers(20, 32))
print(Operations.utils.divide_numbers(300, 60))

data = [
    {
        'Country': 'Mexico',
        'Population': 500
    },
    {
        'Country': 'Colombia',
        'Population': 300
    },
    {
        'Country': 'Argentina',
        'Population': 400
    }
]


def run():
    country = input('Type Country => ')

    result = Operations.repository.population_by_country(data, country)
    print(result)

if __name__ == '__main__':  
    run()


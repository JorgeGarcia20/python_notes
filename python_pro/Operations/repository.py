def greeting(name):
    return f'Hello {name}, welcome!'


def full_name(name, last_name, age):
    return f"i'm {name.title()} {last_name.title()} and i'm {age} years old"


def get_population():
	keys = ['col','bol']
	values = [300,400]
	return keys,values

def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country,data))
    return result

countries = ('Philippines', 'Korea', 'Japan', 'Thailand', 'USA');
cities = ('Tokyo', 'Manila', 'Bangkok');
countries_list = ['Philippines', 'Korea', 'Japan', 'Thailand', 'USA'];


def get_countries():
	return countries

print("Countries", get_countries())


def get_value_by_index(tuple, index):
	return tuple[index]

print("Second Index", get_value_by_index(countries, 2))


def get_value_by_index_range(tuple, index_a, index_b):
	return tuple[index_a:index_b]

print("First two index of a tuple", get_value_by_index_range(countries, 0, 2))


def update_tuples(tuple1, tuple2):
	return tuple1 + tuple2

print("Update Tuples", update_tuples(countries, cities))


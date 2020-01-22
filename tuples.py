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


def repeat_tuples(count):
	tup1 = ('tup1',) * count

	return tup1

print(repeat_tuples(5))


def check_tuple_length(tuple1):

	return len(tuple1)

print("Tuple length", check_tuple_length(cities))


def is_value_exist_in_tuple(tuple1, val):

	return True if val in tuple1 else False

print("Value Exist in tuple", is_value_exist_in_tuple(cities, 'Tokyo'))


def slice_tuple(tuple1):
	return cities[1:]

print("Slice Tuples", slice_tuple(cities))


def is_same_length(tuple1, tuple2):
	return True if len(tuple1) == len(tuple2) else False

print("Is Tuples equal length", is_same_length(cities,cities))


def max_min_values_of_tuple(tuple1):

	dict_tuple = {"Max": max(tuple1), "Min": min(tuple1)}

	return dict_tuple

print("Max and Min values of tuple", max_min_values_of_tuple(cities))


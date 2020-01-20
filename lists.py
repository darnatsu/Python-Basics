
countries = ['Philippines', 'Korea', 'Japan', 'Thailand', 'USA'];
cities = ['Tokyo', 'Manila', 'Bangkok']

def get_countries():
	return countries

print("Countries", get_countries())


def get_index_of(list, value):
	return list.index(value)

print("Index of Japan", get_index_of(countries, 'Japan'))


def get_list_length(list):
	return len(list)

print("Total Countries", get_list_length(countries))


def add_country(list, value):
	list.append(value)
	return list

print("Append", add_country(countries, 'Malaysia'))


def remove_country(list, value):
	list.remove(value)
	return list

print("Remove", remove_country(countries, 'Philippines'))


def sort_list(list):
	list.sort()
	return list

print("Sort", sort_list(countries))


def count_list(list, value):
	return list.count(value)

print("Count", count_list(countries, 'Japan'))


def remove_last_value(list):
	return list.pop()

print("Removed last value", remove_last_value(countries))


def reverse_list(list):
	list.reverse()
	return list

print("Original List", get_countries())
print("Reversed List", reverse_list(countries))


def extend_list(list, list1):
	list.extend(list1)
	return list

print("Extended lists", extend_list(countries, cities))
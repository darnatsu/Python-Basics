
countries = ['Philippines', 'Korea', 'Japan', 'Thailand', 'USA'];

def get_countries():
	return countries

print(get_countries())


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

print("Remove", remove_list(countries, 'Philippines'))


def sort_list(list):
	list.sort()
	return list

print("Sort", sort_list(countries))


def count_list(list, value):
	return list.count(value)

print("Count", count_list(countries, 'Japan'))
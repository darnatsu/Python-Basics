
def short_string(x):
	return x

x = "Lorem ipsum dolor sit amet"
print("Single : " + short_string(x))


def para_string(x):
	return x

x = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nQuisque facilisis nulla ut mauris elementum, in efficitur metus aliquam. \nNulla facilisi. Nulla luctus sagittis tempus. Sed a condimentum justo. \nInterdum et malesuada fames ac ante ipsum primis in faucibus. Maecenas sit amet diam eu ante fermentum rhoncus. \nDonec lorem dolor, gravida ac commodo nec, sodales accumsan lectus. Nullam id ipsum blandit, consectetur felis vitae, bibendum sapien."""
print("Paragraph : " + para_string(x))


def concat_string(x, y):
	return x + y

print("Concat", concat_string('Con', 'cat'))


def repeat_string(string, count):
	return string * count

print("Repeat", repeat_string('Repeat', 4))


def slice_string(string, index):
	return string[index]

print("Slice", slice_string('Slice', 3))


def lower_upper(string):
	return string.upper()

print("Lower to Upper", lower_upper('lowercase to uppercase'))


def upper_lower(string):
	return string.lower()

print("Upper to Lower", upper_lower('UPPERCASE TO LOWERCASE'))


def remove_string_spaces(string, char):
	return string.lstrip()

print("Remove String Spaces", remove_string_spaces("  This is a sentence.", ' '))


def capitalize_string(string):
	return string.capitalize()

print("Capitalize", capitalize_string("test"))


def count_string_length(string):
	return len(string)

print("Count", count_string_length("This is a sentence."))
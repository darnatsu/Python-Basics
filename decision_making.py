# SINGLE IF
def is_profile_existing(val):
	if val >= 1:
		return True

print("Profile Exists", is_profile_existing(2))

def str_more_than_five(str):
	return True if len(str) > 5 else False

print("String is more than 5 characters", str_more_than_five('testesr'))

def is_int(val):
	if isinstance(val, int):
		return True
	else:
		return False

print("Is Int = 10", is_int('x'))

# IF ELSE
def is_foo(x):
	if x == 'foo' :
		return True
	else :
		return False

print("x equals foo", is_foo('foo'))


def is_bar(x):
	if x == 'bar':
		return True
	else:
		return False

print("x equals bar", is_bar('foo'))


def elifs(x):

	if x == 'foo':
		return 'x equals foo'

	elif x == 'bar':
		return 'x equals bar'

	elif x ==  'foobar':
		return 'x equals foobar'
	
	else:
		return False

print("x equals foobar", elifs('foobar'))

def is_number_existing(count, num):

	for x in range(count):
		if x == num:
			return True
		else:
			return False

print("Is number existing in loop range", is_number_existing(20, 25))


def is_character_within_string(str, char):

	str_list = list(str)

	for x in str_list:

		if x == char:
			return True
		else:
			return False


print("Is character existing in string", is_character_within_string('test', 't'))


def nested_ifs(num):

	if num >= 15:
		if num == 8:
			return 'Num is 8'
		else:
			return 'Num is not 8'
	else:
		return 'Num is less than 15'

print("Nested Ifs", nested_ifs(15))

def nested_ifs_with_loop(count):

	for x in range(count):
		if count >= 15:
			if num == 8:
				return 'Num is 8'
			elif num == 15:
				return 'Num is 15'
			else:
				return 'Num is not 8'
		else:
			return 'Num is less than 15'

print("Nested Ifs with loop", nested_ifs_with_loop(5))
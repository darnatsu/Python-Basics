
# INTEGER
def num_int(x):
	return int(x)

print("int", num_int(25))


def num_int(x, y):
	return int(x) + int(y)

print("int", num_int(10, 5))

# LONG
def num_long(x):
	return long(x)

print("long", num_long(515235454154))


def num_long(x, y):
	return long(x) - long(y)

print("long", num_long(515235, 22115))

# FLOAT
def num_float(x):
	return float(x)

print("float", num_float(3.14))


def num_float(x, y):
	return float(x) + float(y)

print("float", num_float(10.20, 3.14))


# COMPLEX
def num_complex(x):
	return complex(x)

print("complex", num_complex(3.14j))
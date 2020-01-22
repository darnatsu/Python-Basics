# WHILE loop
def while_loop():

	x = 0

	while (x < 5):
		print(x)
		x = x + 1

print("WHILE loop")
while_loop()

def while_loop(count):

	x = 0

	while (x < count):
		print(x)
		x = x + 1

print("WHILE loop with count = 5")
while_loop(5)

# FOR loop
def for_loop():

	for y in range(0, 5):
		print(y)

print("FOR loop")
for_loop()

def for_loop(count):

	for x in range(count):
		print(x)

print("FOR loop with count = 3")
for_loop(3)


def for_loop(range_x, range_y):

	for x in range(range_x, range_y):
		print(x)

print("FOR loop with range x and y")
for_loop(5, 10)

# BREAK / CONTINUE
def while_loop_break():

	x = 0

	while (x < 5):
		if(x == 3):
			break
		print(x)
		x = x + 1

print("WHILE loop with break")
while_loop_break()

def while_loop_continue():
	x = 0

	while (x < 10):
		x = x + 1
		if x % 2 == 0:
			continue;
		print(x)

print("WHILE loop with continue")
while_loop_continue()

def for_loop_break():

	for y in range(10):
		if y > 8:
			break
		print(y)

print("FOR loop with break")
for_loop_break()

def for_loop_continue():

	for y in range(10):
		if y % 2 == 0:
			continue
		print(y)

print("FOR loop with continue")
for_loop_continue()


# NESTED loop
def nested_loop():

	a = 0

	while (a < 10):
		b = 5
		while (b <= 8):
			print("b", b)
			b = b + 1
		print("a", a)
		a = a + 1

print("NESTED loop")
nested_loop()

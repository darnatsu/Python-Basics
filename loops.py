# WHILE loop
print("WHILE loop")
x = 0

while (x < 5):
	print(x)
	x = x + 1

# FOR loop
print("FOR loop")

for y in range(0, 5):
	print(y)


# BREAK / CONTINUE
print("WHILE loop with break")
x = 0

while (x < 5):
	if(x == 3):
		break
	print(x)
	x = x + 1

print("WHILE loop with continue")
x = 0

while (x < 10):
	x = x + 1
	if x % 2 == 0:
		continue
	print(x)


print("FOR loop with break")
for y in range(10):
	if y > 8:
		break
	print(y)

print("FOR loop with continue")
for y in range(10):
	if y % 2 == 0:
		continue
	print(y)

# NESTED loop
print("NESTED loop")

a = 0

while (a < 10):
	b = 5
	while (b <= 8):
		print("b", b)
		b = b + 1
	print("a", a)
	a = a + 1


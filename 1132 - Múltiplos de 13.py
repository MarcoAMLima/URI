x = int(input())
y = int(input())

z = x
soma = 0

if x > y:
	x = y
	y = z
while x <= y:
	if x % 13 != 0:
		soma += x
	x += 1
print(soma)
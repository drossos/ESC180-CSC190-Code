def gcd(argA,argB):
	a = argA
	b = argB
	while (a != b):
		if (a > b):
			a = a - b
		else:
			b = b - a
	return a

print("gcd of 76 and 456 is " + str(gcd(76,456)))

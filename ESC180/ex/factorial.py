def fact(x):
	a = 1
	b = 1
	while b <  x+1:
		a = a * b
		b = b + 1
	return a
print("5! = "+ str(fact(5)))
print("9! = "+ str(fact(9)))
 

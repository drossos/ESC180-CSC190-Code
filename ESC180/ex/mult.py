def mult(a,b):
	x = 0
	y = 0;
	while x < a:
		y = y + b
		x = x + 1
	return y

print("3 * 4 = " + str(mult(3,4)))
print("5 * 5 = " + str(mult(5,5)))
	

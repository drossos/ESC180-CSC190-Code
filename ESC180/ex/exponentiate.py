def expo(a,b):
	x = 0
	r = 1
	while x < b:
		r = r * a
		x = x + 1
	return r

print("5^2 " + str(expo(5,2)))
print("7^3 " + str(expo(7,3)))


 

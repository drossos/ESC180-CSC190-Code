def factorial(x):
	i=1
	j=1
	while i < x+1:
		j = i * j
		i = i + 1
	return j

print(str(factorial(5)))


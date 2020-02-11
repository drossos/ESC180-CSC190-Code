def bsqrt(x, acc):
	estimate = x/2
	while (absSub(x,  expo(estimate,2)) > acc):
		estimate = (estimate + (x/estimate)) / 2
	return estimate


def expo(a,b):
	x = 0
	r = 1
	while x < b:
		r = r * a
		x = x + 1
	return r

def absSub(a,b):
	if (a - b < 0):
		return -1*(a-b)
	return a-b
		
print(bsqrt(9,.000000000001))
  

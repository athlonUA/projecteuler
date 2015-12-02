import math;

def p1(n):
	sum = 0

	for i in range(1,n):
		if math.fmod(i,3) == 0 or math.fmod(i,5) == 0:
			sum +=i

	return sum

print p1(1000)


import math;

def p2():
	cur = 0;
	prev = 1;
	prePrev = 0;
	sum = 0;
	
	while 1:
		cur = prePrev + prev
		if cur < 4000000:
			sum = sum + (cur if math.fmod(cur,2) == 0 else 0)
		else:
			break

		prePrev = prev
		prev = cur

	return sum

print p2()

def solution(x, y):
	# Your code here
	a = int(x)
	b = int(y)


	i = 0;
	while ( True ):
		# print (a, b)
		if (a > b):
			# added case where one number is 10 times greater than the other
			# to save steps/time
			if ( a > 10*b ):
				i += int (a/b) - 1
				a = a - (int(a/b) - 1)*b
			else:
				a = a-b
				i += 1
		elif ( b > a ):
			# added case where one number is 10 times greater than the other
			# to save steps/time
			if ( b > 10*a ):
				i += int (b/a) - 1
				b = b - (int(b/a) - 1)*a
			else:
				b = b - a
				i += 1
		elif ( a == 1 and b == 1):
			return str(i)
		else:
			return "impossible"

print ( solution ("2", "1"))
def smaller (a, b):
	s1 = list (map ( int, a.split('.') ));
	s2 = list (map ( int, b.split('.') ));
	
	# compare the first digit
	if ( s1[0] < s2[0] ):
		return True;
	elif ( s1[0] > s2[0] ):
		return False;
	
	# first digit equal, compare the second digit
	else:
		# version with no second digit is smaller
		if ( len(s1) == 1 ):
			return True;
		elif ( len(s2) == 1 ):
			return False;

		# compare the second digit
		else:
			if ( s1[1] < s2[1] ):
				return True;
			elif ( s1[1] > s2[1] ):
				return False;

			# second digit equal, compare the third digit
			else:
				# version with no third digit is smaller
				if ( len(s1) == 2 ):
					return True;
				elif ( len(s2) == 2 ):
					return False;
				
				# compare the third digit
				else:
					if ( s1[2] < s2[2] ):
						return True;
					elif ( s1[2] > s2[2] ):
						return False;
					else:
						# error
						return True;
def swap (l, i1, i2):
	temp = l[i1];
	l[i1] = l[i2];
	l[i2] = temp;


def partition ( l, low, high ):

	pivot = l[high]
	swap_pt = low - 1

	for i in range (low, high):
		if ( smaller( l[i], pivot ) ):
			# print (l[i], " is smaller than ", pivot)
			swap_pt += 1
			swap(l, i, swap_pt)

	swap (l, swap_pt+1, high)

	return swap_pt + 1

def qsort (l , low, high):
	if (low < high):

		pivot = partition (l, low, high);

		qsort (l, low, pivot-1)
		qsort (l, pivot+1, high)


def solution(l):
	qsort(l, 0, len(l)-1);
	return l;
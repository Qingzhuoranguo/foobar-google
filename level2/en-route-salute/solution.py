s = "<<>><"
def solution(s):
	# Your code here
	solute = 0;
	for i in range ( len(s) ):
		if (s[i] == '>'):
			print (i, s[i])
			for j in range (i+1, len(s)):
				if (s[j] == '<'):
					solute += 1
	return solute*2
print (solution(s))
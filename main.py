
def convertString(S, a, b):
	print(S)
	
	# Stores the size of the string
	N = len(S)

	# Loop to iterate over the string
	for i in range(0, N // 2):

		# If one of S[i] or S[N-i-1] is
		# equal to '?', replace it with
		# corresponding character
		if (S[i] == '?' and S[N - i - 1] != '?'):
			S[i] = S[N - i - 1]
		elif (S[i] != '?' and S[N - i - 1] == '?'):
			S[N - i - 1] = S[i]
		
	# Subtract the count of 0 from the
	# required number of zeroes
	cnt_0 = 0
	for i in range(0, N):
		if (S[i] == '0'):
			cnt_0 += 1
	
	a = a - cnt_0

	# Subtract the count of 1 from
	# required number of ones
	cnt_1 = 0

	for i in range(0, N):
		if (S[i] == '0'):
			cnt_1 += 1


	b = b - cnt_1

		# Traverse the string
	for i in range(0, N // 2):

		# If both S[i] and S[N-i-1] are '?'
		if (S[i] == '?' and S[N - i - 1] == '?'):

			# If a is greater than b
			if (a > b):

				# Update S[i] and S[N-i-1] to '0'
				S[i] = S[N - i - 1] = '0'

				# Update the value of a
				a -= 2
			else:

				# Update S[i] and S[N-i-1] to '1'
				S[i] = S[N - i - 1] = '1'

				# Update the value of b
				b -= 2
		

	# Case with middle character '?'
	# in case of odd length string
	if (S[N // 2] == '?'):

			# If a is greater than b
			if (a > b):

				# Update middle character
				# with '0'
				S[N // 2] = '0'
				a -= 1
			else:

				# Update middle character
				# by '1'
				S[N // 2] = '1'
				b -= 1
			
	# Return Answer
	if (a == 0 and b == 0):
			return S
	else:
			return "-1"

# Driver Code

a = 5
b = 4
S = "?" * (a+b)
S = list(S)

print("".join(convertString(S, a, b)))

# This code is contributed by gfgking

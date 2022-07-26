def uniquenumbers3(arr):
	l = [0 for i in range(65)]
	for i in range(len(arr)):
		b = bin(arr[i])[2:]
		c = 0
		for j in range(len(b) - 1, -1, -1):
			l[64 - c] += int(b[j])
			c += 1

	newstr = ""
	for i in range(65):
		newstr += str(l[i] % 3)

	print(int(newstr, 2))


n = int(input())
arr = list(map(int, input().split()))
uniquenumbers3(arr)

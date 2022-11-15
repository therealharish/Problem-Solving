n = 6
d = {}
d[2] = 1
d[3] = 1

for i in range(4, n+1):
	ans = 0
	for j in range(2, i):
		ans += d[i-j+1]*d[j]
	d[i] = ans

print(d[n])
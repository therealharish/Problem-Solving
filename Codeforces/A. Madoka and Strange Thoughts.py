# in copy pg 2
t = int(input())
for _ in range(t):
	n = int(input())
	ans = n
	ans += (n // 2) * 2
	ans += (n // 3) * 2
	print(ans)

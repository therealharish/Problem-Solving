t = int(input())
for _ in range(t):
    n = list(map(int, input().split()))
    work = n[0] * 4
    work += n[1]
    print(work)

t = int(input())
for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    res = 0
    mod = 1000000007

    for ele in a:
        if not (ele & 1):
            res += 1

    ans = 1
    for i in range(res):
        ans *= 2
        ans %= mod

    print(ans)
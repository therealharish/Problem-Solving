primes = (2, 3, 5, 7, 11, 13, 17, 19)
t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    for i in range(1, 2**8):
        denom = 1
        setBits = bin(i).count("1")
        for j in range(8):
            if (i & (1 << j)):
                denom = denom * primes[j]
        if (setBits & 1):
            ans += n // denom
        else:
            ans -= n // denom
    print(ans)

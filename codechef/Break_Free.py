mod = 10**9 + 7

t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    
    c = sum(1 for num in a if num % 2 == 0)
    
    temp = 1
    for i in range(c):
        temp = (temp * 2) % mod
        
    if c == n:
        print(temp - 1)
    else:
        print(temp)
    
    t -= 1

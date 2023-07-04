n = int(input())
m = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
win = [0 for i in range(n)]
for i in range(m):
    val = 0
    best = 0
    for j in range(n):
        # print(val, best)
        if data[j][i] > val:
            val = data[j][i]
            best = j
    win[best] += 1
    # print(win)
m = max(win)
a = 0
for i in range(n):
    if win[i] == m:
        a = i+1
        break
return a
    
    
        
        

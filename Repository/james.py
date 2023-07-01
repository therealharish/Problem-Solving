
def stoneGame(piles):

    dp = {}
    def f1(i, j):
        if (i, j) in dp:
            return dp[(i, j)]
        if i > j:
            return 0
        else:
            dp[(i, j)] = max(piles[i]+f2(i+1, j), f2(i, j-1)+piles[j])
            return dp[(i, j)]
    
    def f2(i, j):
        if i > j:
            return float('inf')
        else:
            return min(f1(i+1, j), f1(i, j-1))

    james = f1(0, len(piles)-1)
    return james


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
print(stoneGame(arr))
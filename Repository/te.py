

def solve(num, soldierPosition, posSoldier):
    
    mp = [i for i in range(1, num + 1)]
    for x, y in soldierPosition:
        arr = mp[x - 1:y]
        for i in range(x - 1, y):
            mp[i] = arr.pop()

    return mp[posSoldier - 1]

num = 10
soldierPosition = [[1, 5], [6, 10]]
posSoldier = 1
print(solve(num, soldierPosition, posSoldier))

num = 10
soldierPosition = [[5, 9], [2, 3]]
posSoldier = 10
print(solve(num, soldierPosition, posSoldier))

        
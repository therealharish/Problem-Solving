
def asteroidCollision(strength, direction):
    s = []
    take = []
    for i in range(len(strength)):
      take.append(strength[i]*direction[i])
    for i in range(len(take)):
        a = take[i]
        while s and s[-1] > 0 and a < 0:
            if s[-1] + a < 0: s.pop()
            elif s[-1] + a > 0: break    
            else: s.pop(); break
        else: s.append(i)        
    return s  

strength=  [5, 10, 5]
direction = [1, 1, -1]
strength=  [8,8]
direction = [1, -1]
ans = asteroidCollision(strength,direction)
print(ans)
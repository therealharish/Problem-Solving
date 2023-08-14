i = int(input())

def solve(i):
    if i >= 30 and i <= 50:
        return "D"
    if i >= 51 and i <= 60:
        return "C"
    if i >= 61 and i <= 80:
        return "B"
    if i >= 81 and i <= 100:
        return "A"
    
    
m = max((0.5*base1*height1), (0.5*base2*height2))
return round(m, 1)  
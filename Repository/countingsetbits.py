# Method 1


def countsetbitsbycheckinlastbit(n):
    count = 0
    while (n != 0):
        count += (n & 1)
        n = n >> 1
    return count


def countsetbitsbyremovinglastbit(n):
    count = 0
    while (n > 0):
        n = n & (n - 1)
        count += 1
    return count


n = 15
print(countsetbitsbyremovinglastbit(n))

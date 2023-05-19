def minion_game(string):
    
    vowels = 'AEIOU'
    countStuart = 0
    countKevin = 0
    for i in range(len(string)):
        if string[i] in vowels:
            countKevin += len(string)-i
        else:
            countStuart += len(string)-i
    if countStuart > countKevin:
        print("Stuart", countStuart)
    elif countStuart < countKevin:
        print("Kevin", countKevin)
    else:
        print("Draw")
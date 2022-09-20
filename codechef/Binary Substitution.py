# in notes 1 pg 28

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    countzero = s.count('0')
    countone = s.count('1')
    if ((countone == 0 or countzero == 0)):
        print(len(s), 0)
        continue
    replace = '1' if countzero > countone else '0'
    ans = []
    count = 0
    while (countzero != countone):
        for i in range(len(s)):
            if (s[i] != s[i + 1]):
                s = s[0:i] + replace + s[i + 2:]
                ans.append((i + 1, i + 2, replace))
                count += 1
                countzero = s.count('0')
                countone = s.count('1')
                replace = '1' if countzero > countone else '0'
                break

    if (countzero == countone):
        count += 1
        ans.append((1, len(s), replace))

    print(1, count)
    if (ans):
        for i in ans:
            print(i[0], i[1], int(i[2]))

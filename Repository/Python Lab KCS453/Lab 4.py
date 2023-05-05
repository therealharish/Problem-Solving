from collections import Counter

file = open("Repository/txtfiles/file1.txt", "r")
f = file.read()
lis = f.split(" ")
s = Counter(lis)
m = max(s, key = s.get)
print(m)
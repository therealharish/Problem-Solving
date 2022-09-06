s = "203"
k = 3
l = []
for i in s:
  l.append(int(i))
l.sort(reverse = True)
for i in range(k):
  l.pop(0)
print(sum(l))
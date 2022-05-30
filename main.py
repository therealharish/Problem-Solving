s = "ABCDDCEFFEBGAG"
l = []
d = {}
c=3
count = 0
for i in s:
  print(l)
  if i in l:
    l.remove(i)
  else:
    if(len(l)==c):
      d[i] = 0
    else:
      l.append(i)
print(len(d))
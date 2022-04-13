l=[2,3,3,2,1]
n=len(l)

for i in range(len(l)):
  x = l[i]
  l[x%n]+=n

for i in range(len(l)):
  l[i]=l[i]//n
print(l)



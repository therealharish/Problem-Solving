l=[0,0,6,7,5,8,9,0,20,0,-2]

x=-1;
for i in range(len(l)):
  if(l[i]==0):
    l[x], l[i] = l[i], l[x]
    x+=1
print(l)
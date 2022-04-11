l = [2,5,3,7,8,1,9]
# l=[5,7,4,9,8,10]
c = []
s=[]
i=0;
for i in range(len(l)):
  s = l[i+1:]
  flag=1
  while(s):
    if(s[0]>l[i]):
      c.append(s[0])
      flag=0
      break;
    else:
      s.pop(0)
  if(flag):
    c.append(-1)
print(c)
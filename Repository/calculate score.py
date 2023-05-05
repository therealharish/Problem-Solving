s=input();
l=[];
x=-1;
for i in range(len(s)):
  if(s[i]=="+"):
    if(len(l)==1):
      continue;
    else:
      a=int(l.pop(x));
      x-=1;
      b=int(l.pop(x));
      x-=1;
      l.append(str(a+b))
      x+=1
  elif(s[i]=="D"):
    a=int(l.pop(x));
    x-=1;
    l.append(str(a*2))
    x+=1
  elif(s[i]=="C"):
    a=l.pop(x)
    x-=1
  else:
    l.append(s[i]);
    x+=1;
l=map(int, l)
print(sum(l))
      
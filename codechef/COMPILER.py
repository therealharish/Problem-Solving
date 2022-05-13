t = int(input())
for _ in range (t):
  s= input()
  l=[]
  for i in range(len(s)):
    if(s[i]=="<"):
      l.append(s[i])
    else:
      if len(l)!=0 and l[-1]=="<" :
        l.pop()
      else:
        l.append(s[i])
  print(len(s)-len(l))
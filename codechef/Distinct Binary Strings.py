t = int(input())
for _ in range (t):
  n = int(input())
  s = input()
  d={}
  count=1;
  for i in range(len(s)-1):
    if(s[i]!=s[i+1]):
      count+=1
  print(count)
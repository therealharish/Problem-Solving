t = int(input())
while(t):
  d = list(map(int, input().split()))
  s = list(map(int, input().split()))
  ds = sum(d);
  ss = sum(s);
  if(ds>ss):
    print("Dragon")
  elif(ds==ss and d[0]>s[0]):
    print("Dragon")
  elif(ds==ss and d[0]==s[0] and d[1]>s[1]):
    print("Dragon")
  elif(ds==ss and d[0]==s[0] and d[1]==s[1]):
    print("Tie")
  else:
    print("Sloth")
  
      
  t-=1
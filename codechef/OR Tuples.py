t = int(input())
for _ in range (t):
  a,b,c = map(int, input().split())
  ans = 1
  for i in range(20):
    k=0
    if(a&1):
      k+=1
    if(b&1):
      k+=1
    if(c&1):
      c+=1
    if(k==3):
      ans*=4
    elif(k==2):
      ans*=1
    elif(k==1):
      break
    else:
      ans*=1

    a=a>>1
    b=b>>1
    c=c>>1
  print(ans)

  
    
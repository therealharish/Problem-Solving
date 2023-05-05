t = int(input())
while(t):
  n = list(map(int, input().split()))
  center = [n[0]+1//2, n[0]+1//2]
  x=abs(center[0]-n[1])
  y=abs(center[1]-n[2])
  sum=x+y;
  if(sum%2==0):
    print("0");
  else:
    print("1");
      
  t-=1
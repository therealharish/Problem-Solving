t = int(input())
while(t):
  a = list(map(int, input().split()))
  n=a[1]
  if(n%2==0 and a[0]==1):
    print("Even")
  elif(n%2!=0 and a[0]==1):
    print("Odd")
  else:
    print("Impossible")
  t-=1
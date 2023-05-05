t = int(input())
while(t):
  n = list(map(int, input().split()))
  count =0;
  for i in range (n[0]):
    if(i%2!=0):
      continue;
    for j in range(n[1]):
      if(j%2==0):
        count+=1
  print(count)
      
  t-=1
t = int(input())
for _ in range (t):
  n,k = map(int, input().split())
  s = input();
  l =0 
  h = n-1;
  count=0;
  while(l<h):
    if(s[l]!=s[h]):
      count+=1;
    l+=1;
    h-=1;
  if(count <= k):
    if(len(s)%2==1):
      print("YES")
    else:
      if ((k-count)%2==0):
        print("YES")
      else:
        print("NO")
  else:
    print("NO")
from collections import Counter
n = int(input())
flag = 0;
count = 0;
while(n):
  m = int(input())
  b = list(map(int, input().split()))
  temp = Counter(b)
  a=list()
  for x in temp.keys():
    a.append(x)
  a.sort();
  for i in range(1,len(a)+1):
    new = a[:i];
    elem = new[int((len(new)-1)/2)]
    if elem in temp.keys():
      if(temp[elem]==0):
        print("-1");
        flag = 1;
        break;
      else:
        temp[elem] = temp[elem]-1;
        count = count +1;
    else:
      print("-1")
      flag = 1;
      break;
  for i in range(1,len(a)+1):
    new = a[-i:];
    elem = new[int((len(new)-1)/2)]
    if elem in temp.keys():
      if(temp[elem]==0):
        print("-1");
        flag = 1;
        break;
      else:
        temp[elem] = temp[elem]-1;
        count = count+1;
    else:
      print("-1")
      flag = 1;
      break;

  if(flag == 0):
    for i in temp.values():
      if(i>0):
        print(-1);
        flag = 1

  if(flag == 0):
    for i in a:
      print(i, end=" ")

  print()
  n=n-1;
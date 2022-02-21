test = int(input())
def total(num):
  totalsum = 0;
  for i in range (num+1):
    totalsum = totalsum+i;
  return totalsum

while(test!=0):
  a,b=map(int,input().split())
  tempsum=b;
  while(a!=0):
    sum=0;
    sum = sum + total(tempsum);
    tempsum = sum;
    a=a-1;
  print(sum)
  test-=1



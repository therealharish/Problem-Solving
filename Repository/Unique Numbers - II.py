def uniquenumbers(arr):
  ans = 0
  for i in range(len(arr)):
    ans = ans^arr[i]
  temp = ans
  pos = 0
  while((temp&1)==0):
    pos+=1
    temp >> 1
  mask = 1<<pos
  x = 0
  y = 0
  for i in arr:
    if(i&mask):
      x = x^i
  y = ans^x
  print(x,y)
  
arr = [1,1,3,2]
uniquenumbers(arr)

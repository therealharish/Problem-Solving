# https://www.geeksforgeeks.org/print-all-subarrays-with-0-sum/

l = [0,0,5,5,0,0]
i,j=0,0
flag=0
while(i<j and i<len(l) and j<len(l)):
  a = sum(l[i:j+1])
  if(a<0):
    j+=1
  elif(a==0):
    print(l[i:j+1])
  else:
    j+=1
    i=j
  
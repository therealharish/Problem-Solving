# https://www.geeksforgeeks.org/print-all-subarrays-with-0-sum/

l = [0,0,5,5,0,0]
l = [6,-1,-3,4,-2,2,4,6,-12,-7]

d = {}
count = 0
s=0
out  = []
for i in range(len(l)):
  s+=l[i]
  if s == 0:
    out.append(l[0:i+1])
  if s in d:
    print(d)
    a = d[s]
    print(a)
    out.append(l[a+1: i+1])
  
  d[s] = i
    

print(out)
    
  



  
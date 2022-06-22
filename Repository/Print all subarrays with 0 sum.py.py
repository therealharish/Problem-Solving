# https://www.geeksforgeeks.org/print-all-subarrays-with-0-sum/

l = [0,0,5,5,0,0]
l = [6,-1,-3,4,-2,2,4,6,-12,-7] 

# prefix = l[:]
# for i in range(1, len(prefix)):
#   prefix[i] = prefix[i]+prefix[i-1]

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
    for a in d[s]:
      out.append(l[a+1: i+1])
  
  if s in d:
    a = d[s]
    a.append(i)
    d[s] = a
  else:
    d[s] = [i]
    

print(out)
    
  



  
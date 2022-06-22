# 2304. Minimum Path Cost in a Grid

l = [3,34,4,12,5,2]
k = 9
l = [4,5,6,10,23,11]
k = 12
l = [2,6,10,20,30]
k=  42

# i = 0
# j = 0

# while(i<=j and i<len(l) and j<len(l)):
#   s = sum(l[i:j+1])
#   if(s>k):
#     i=i+1
#     j=i
#   elif (s==k):
#     print("True")
#     break
#   elif(s<k):
#     j+=1
recur(l, 0, 0)

def recur(l,i, s):
  if(s>k):
    i+=1
    return False
  else:
    s+=l[i]
    
    
  

def finddiff(a,b):
  count=0
  for i in range(len(a)):
    if(a[i]!=b[i]):
      count+=1
  return count

def highestValuePalindrome(s, n, k):
  l = list(s)
  
  s1 = l[:n//2]
  s2 = l[n//2:]
  i=0
  if(len(s)%2!=0):
    leverage = [s2.pop(0)]
  else:
    leverage = []
    
  s2.reverse()
  diff = finddiff(s1, s2)
  
  if(diff>k):
    return "-1"
    
  while(k and diff<=k):
    
    if(k>1):
      if(k>diff):
        if(s1[i]!='9' and s2[i]!='9'):
          if(s1[i]==s2[i]):
            diff+=1
          s1[i]='9'
          s2[i]='9'
          k-=2
          diff-=1
        elif(s1[i]=='9' and s2[i]!='9'):
          s1[i]='9'
          k-=1
          diff-=1
        elif(s2[i]=='9' and s1[i]!='9'):
          s2[i]='9'
          k-=1
          diff-=1
          
      elif(k==diff):
        if(s1[i]<s2[i]):
          s1[i] = s2[i]
          k-=1
          diff-=1
        elif(s1[i]>s2[i]):
          s2[i] = s1[i]
          k-=1
          diff-=1
          
    elif(k==1):
      if(n%2!=0):
        leverage = ['9']
        k-=1
        
      else:
        if(s1[i]<s2[i]):
          s1[i] = s2[i]
          k-=1
          diff-=1
        elif(s1[i]>s2[i]):
          s2[i] = s1[i]
          k-=1
          diff-=1
    
        
    i+=1

n=4
k=4
s="3943"
print(highestValuePalindrome(s, n, k))
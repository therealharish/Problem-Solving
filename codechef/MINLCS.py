# cook your dish here
t = int(input())
for _ in range(t):
  l = int(input())
  a = input()
  b = input()
  aarr = [0]*26
  barr = [0]*26
  for i in a:
    aarr[ord(i)-97]+=1
  for i in b:
    barr[ord(i)-97]+=1

  m = 0
  for i in range(26):
    m = max(m, min(aarr[i], barr[i]))
  print(m)
    
    
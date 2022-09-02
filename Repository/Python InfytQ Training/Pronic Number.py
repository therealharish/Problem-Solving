s = "93012630"
i = 1
j = 2
while(True):
  if(i*j>int(s)):
    break
  else:
    m = i*j
    if(str(m) in s):
      print(m)
  i+=1
  j+=1

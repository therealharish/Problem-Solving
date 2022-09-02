s = "Hello#81@21349"
l = set()
for i in s:
  if(i.isnumeric()):
    l.add(int(i))
l = list(l)
print(l)
l.sort(reverse = True)
if(l[-1]&1):
  temp = -1
  for i in range(len(l)-1, -1, -1):
    if(l[i]%2==0):
      temp = l.pop(i)
      break
  if(temp==-1):
    print("None")
  else:
    l.append(temp)
l = list(map(str, l))
print("".join(l))
  
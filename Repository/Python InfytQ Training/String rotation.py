s = "rhdt:246"
# s = "ghftd:1246"

num = s.split(":")[1]
s = s.split(":")[0]

dig = 0
for i in num:
  dig+=int(i)**2

if(dig&1):
  ans = s[len(s)-2:]+s[0:len(s)-2]
else:
  ans = s[1:]+s[0]

print(ans)
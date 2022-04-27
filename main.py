s="3523014"

for i in range(len(s)):
  n = i
  sum = 0
  sub=""
  news=""
  while(n<len(s) and sum<10):
    sum+=int(s[n])
    sub+=s[n]
    n+=1
  if(sum==10):
    if(n!=len(s) and s[n]=='0'):
      news = sub
      sub+='0'
      
    print(sub)
    if news:
      print(news)
  
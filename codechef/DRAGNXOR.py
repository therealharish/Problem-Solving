def binary(num):
  bin = "";
  while(num>0):
    bin = str(num%2) +bin
    num = num//2
  return bin


t = int(input())
while(t):
  n = list(map(int, input().split()))
  N, A, B = n[0], n[1], n[2]
  if(A<B):
    A,B=B,A
  a = binary(A)
  b = binary(B)
  
  
  
  if(len(a)<N):
    m = N-len(a)
    str1 = "0"*m
    a = str1+a

  if(len(b)<N):
    m = N-len(b)
    str1 = "0"*m
    b = str1+b
  
  counta0 = a.count('0')
  counta1 = a.count('1')
  countb0 = b.count('0')
  countb1 = b.count('1')

 
  newa = "1"*counta1
  newa+= "0"*counta0
  newb = "0"*countb0
  newb+="1"*countb1
  ba = N-1;
  bb=N-1;
  la=[]
  la[:0] = newa
  lb=[]
  lb[:0] =newb
  i=0;

  for i in range(N):
    if(newa[i]=='1' and newb[i]=='1' and la[ba] == '0'):
      la[ba] = '1'
      la[i] ='0'
      ba-=1;
    elif(newa[i]=='0' and newb[i]=='0' and lb[bb] == '1'):
      lb[ba] ='0'
      lb[i] ='1'
      bb-=1

  la = "".join(la)
  lb = "".join(lb)
      

  ans = int(la,2)^int(lb,2)
  print(int(ans))

  t-=1
  
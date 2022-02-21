# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
l=list()
m=0;
def ischar(s):
  for i in s:
    if i.isalpha():
      return 0;
  return 1;

for i in range (n):
  l.append(input())
while(m<len(l)):
  s = l[m];
  s=s+' ';
  try:
    x = s.index('.');
    if(s[x+1]==' '):
      print("False")
    elif(s[1]=='+' or s[1]=='-'):
      print("False");
    elif(s.count('.')>1):
      print("False");
    elif (ischar(s)==0):
      print("False")
    else:
      print("True")
    m+=1;
  except Exception as e:
    print("False");
    m+=1;



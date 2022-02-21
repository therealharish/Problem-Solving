#lex_auth_01269442760027340879

def find_smallest_number(num):
  i=1;
  while(True):
    no=[];
    for j in range(1,i+1):
      if(i%j==0):
        no.append(j)
    if(len(no)==num):
      return i;
      break;
    else:
      i+=1

    

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)
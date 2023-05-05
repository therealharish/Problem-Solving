#lex_auth_01269446157664256093

def check_prime(number):
  flag=0;
  for i in range(number):
    if(number%i==0):
      flag+=1;
  if(flag==1):
    return True;
  else:
    return False;

def rotations(num):
    i=0;
    l=[];
    while(i<len(num)):
      rem=int(num % 10)
      num=int(num / 10)
      num=int((rem * (10 ** (length - 1)) + num))
      l.append(num)
      i+=1;
      print(l)

def get_circular_prime_count(limit):
    pass #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.

#Provide different values for limit and test your program
print(get_circular_prime_count(1000))
#lex_auth_01269442963365068878

def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
  newl=[]
  for i in list_of_factors:
    if(is_prime(i,i//2)):
      newl.append(i)
  return max(newl)

def find_f(num):
  l=find_factors(num)
  return find_largest_prime_factor(l)  

def find_g(num):
  sum=0;
  for i in range(num, num+9):
    sum+=find_f(i);
  return sum;

#Note: Invoke function(s) from other function(s), wherever applicable.

print(find_g(10))
#lex_auth_01269443664174284882
def nearest_palindrome(number):
  i=number+1;
  while(True):
    num=i
    rev=0;
    while(num!=0):
      rev=rev*10+num%10;
      num=num//10;
    if(rev==i):
      return rev;
    else:
      i+=1;
      
number=12300
print(nearest_palindrome(number))
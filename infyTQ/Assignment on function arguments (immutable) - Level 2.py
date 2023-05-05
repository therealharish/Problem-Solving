#lex_auth_01269441810970214471
from collections import Counter

def check_double(number):
  num2 = str(number*2)
  num1 = str(number)
  if(Counter(num1)==Counter(num2)):
    return True
  else:
    return False
    

#Provide different values for number and test your program
print(check_double(125874))
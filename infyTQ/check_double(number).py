#lex_auth_01269441810970214471

def check_double(number):
  double = number*2;
  number=str(number);
  double = str(double)
  if(len(double)!=len(number)):
    return False
  else:
    for i in range(len(number)):
      if(number[i]==double[i]):
        return False
    return True
      

#Provide different values for number and test your program
print(check_double(125874))
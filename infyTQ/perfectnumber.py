#lex_auth_01269446533799116898

def check_perfect_number(number):
  sum=0;
  if(number==0):
    return 0;
  for i in range (1,number//2 +1):
    if(number%i==0):
      sum=sum+i;
  if sum==number:
    return 1;
  else:
    return 0;
        

def check_perfectno_from_list(no_list):
  newl=[];
  for i in no_list:
    if(check_perfect_number(i)):
      newl.append(i);
  return newl

perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)
#lex_auth_0127382164803993601239

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    if(filter_func==None):
      return sum(list_of_num)
    elif(filter_func==even):
      s=even(list_of_num);
      return sum(s);
    else:
      s=odd(list_of_num);
      return sum(s);

def even(data):
  l=[];
  for i in data:
    if(i%2==0):
      l.append(i)
  return l

def odd(data):
  l=[];
  for i in data:
    if(i%2!=0):
      l.append(i)
  return l

sample_data = range(1,11)

print(sum_of_numbers(sample_data,even))
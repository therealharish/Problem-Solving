#lex_auth_01269443477535129681

def find_duplicates(list_of_numbers):
  l=[];
  d={};
  for x in list_of_numbers:
    if(x in list(d.keys())):
      d[x]+=1;
    else:
      d[x]=1;
  for x,y in d.items():
    if(y>1):
      l.append(x)
  return l
    

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
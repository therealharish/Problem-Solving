#lex_auth_01269438947391897654

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
  av=sum(list_of_marks)/10;
  count=0;
  for i in list_of_marks:
    if i > av:
      count+=1;

  percentage = (count/10)*100;
  return percentage

def sort_marks():
  l=list(list_of_marks)
  l.sort()
  return l


def generate_frequency():
  l=list();
  for i in range(0,26):
    l.append(0);
  for i in list_of_marks:
    l[i]+=1;
  return l

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
#lex_auth_01269438594930278448

def find_pairs_of_numbers(num_list,n):
  d={};
  for i in range (len(num_list)):
    d[num_list[i]] = n-num_list[i]
  count = 0;
  lv=list(d.values())
  lk=list(d.keys())
  for i in lv:
    if i in num_list:
      count+=1;
  return count//2

num_list=[1, 2, 7, 4, 5, 6, 0, 3]
n=6
print(find_pairs_of_numbers(num_list,n))
#lex_auth_0127382283825971201450

def max_frequency_word_counter(data):
  word=""
  frequency=0
  d={};
  for i in data:
    if i in d.keys():
      d[i]+=1;
    else:
      d[i]=0;
  print(d)


#Provide different values for data and test your program.
data="Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)
#lex_auth_01269444890062848087

def find_correct(word_dict):
    l=[0,0,0]
    for x,y in word_dict.items():
      print(x,y)
      wrong=0;
      if(len(x)!=len(y)):
        l[2]+=1;
      else:
        for i in range(len(x)):
          if(x[i]!=y[i]):
            wrong+=1;
        if(wrong==0):
          l[0]+=1;
        elif(wrong==2 or wrong==1):
          l[1]+=1
        else:
          l[2]+=1
    return l;

word_dict={'ALWAYS': 'ALLISWELL', 'VENDOR': 'VENDING', 'MIND': 'MUND', 'RADIO': 'RADICAL', 'CHECK': 'CHEK'}
print(find_correct(word_dict))
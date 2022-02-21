#lex_auth_0127382206342184961397

def check_anagram(data1,data2):
    if(len(data1)!=len(data2)):
      return False
    else:
      for i in range(len(data1)):
        if(data1[i]==data2[i]):
          return False
      return True

print(check_anagram("eat","tea"))



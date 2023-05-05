#lex_auth_01269444195664691284

def encrypt_sentence(sentence):
    l = sentence.split(" ")
    s=""
    for i in range(len(l)):
      word = str(l[i])
      if(i%2==0):
        s+= word[::-1]+" " 
      else:
        v=""
        c=""
        for j in word:
          if (j in "aeiou"):
            v+=j
          else:
            c+=j;
        s+=c+v+" "
    return s.strip()
sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)


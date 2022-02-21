#lex_auth_012693825794351104168

def find_common_characters(msg1,msg2):
    newstr=""
    if(len(msg1)<len(msg2)):
      msg = msg1
      check = msg2
    else:
      msg = msg2;
      check = msg1
    for i in range (len(msg)):
      x = msg[i]
      for j in range (len(check)):
        if(check[j]==x and x!=' '):
          newstr=newstr+x;
          break
    if(len(newstr)==0):
      return -1;
    else:
      return newstr

#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
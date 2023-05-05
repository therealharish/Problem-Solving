#lex_auth_012693816331657216161

def encode(message):
    encoded = "";
    count = 1;
    for i in length(len(message)-1):
      if(message[i]==message[i+1]):
        count=count+1;
      else:
        encoded=str(count)+message[i];

    return encoded
        
        

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
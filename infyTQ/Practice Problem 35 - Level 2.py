#lex_auth_0127136447430656001216

def convert_to_roman(num):
  ansString = ""
  while(num):
    if(len(str(num))==4):
      n = num//1000
      ansStr = "M"*n
      num = num%1000
    if(len(str(num))==3):
      n = num/100
      
    


for num in range(1,5000):    
    print(num," : ",convert_to_roman(num))
#lex_auth_012693816779112448160

def calculate(distance,no_of_passengers):
  fuel=70*(distance/10);
  r=80*no_of_passengers;
  profit=r-fuel;
  if(profit<0):
    return -1;
  else:
    return profit;
  
  



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
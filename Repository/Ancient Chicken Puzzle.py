#lex_auth_012693810762121216155

import math

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    error=1
    check=1
    i=0;

    if(legs%2!=0):
      error=1;
    else:
      while(i<=heads):
        nrl=i*4;
        ncl=legs-nrl;
        rhead=(nrl//4)
        chead=(ncl//2)
        if((rhead+chead==heads) and (nrl+ncl==legs)):
          chicken_count=chead;
          rabbit_count=rhead;
          error=0;
          break;
        else:
          i+=1;




    if(error==0):
      print(chicken_count,rabbit_count)
    else: 
      print(error_msg)


    

#Provide different values for heads and legs and test your program
solve(35,94)
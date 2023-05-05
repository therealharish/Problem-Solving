#lex_auth_012693813706604544157

def find_max(num1, num2):
    max_num=-1
    l=list();
    if(num1>num2):
      return -1
    else:
      for i in range(num1, num2+1):
        twodigits=False
        divthree=False
        divfive=False
        nums=str(i)
        if(len(nums)==2):
          twodigits=True;
          if((int(nums[0])+int(nums[1]))%3==0):
            divthree=True;
            if(i%5==0):
              divfive=True;
        if(twodigits and divthree and divfive):
          l.append(i)
    if(len(l)==0):
      return -1;
    else:
      max_num=max(l)
      return max_num
  

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)
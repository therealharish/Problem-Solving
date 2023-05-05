#lex_auth_0127136008767324161169

def close_number(num1,num2,num3):
  s = set(num1, num2, num3)
  ma = max(s)
  mi = min(s)
  if((mi+1 in s and mi+2 not in s) and (ma-1 in s and ma-2 not in s):
    return True
  else:
    return False
  

    
    
print(close_number(5,4,2))
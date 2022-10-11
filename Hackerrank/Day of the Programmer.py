#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#


def dayOfProgrammer(year):

  if(year == 1918):
    return "26.09.1918"
  Leap = False
  if(year < 1918 and year%4==0):
    Leap = True
  elif(year>1918):
    if(year%400 == 0):
      Leap = True
    elif(year%4==0 and year%100!=0):
      Leap = True

  if Leap:
    return "12.09."+str(year)
  else:
    return "13.09."+str(year)
  
    
    
      
        
  
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

#lex_auth_0127136332814499841204

def sum_of_elements(num_list,number):
    s = 0
    i = 0
    while(i<len(num_list)):
        if(num_list[i] == number):
            if(i>0 and s>0):
              s-=num_list[i-1]
            i+=1
        else:
            s+=num_list[i]
        i+=1
            
    result_sum = s
    return result_sum
      
num_list=[1,7,3,4,1,7,10,5]
number=7
print(sum_of_elements(num_list, number))
#lex_auth_0127136357873991681201

def exchange_list(number_list):
    n = len(number_list)
    l1 = number_list[:n//2]
    l2 = number_list[n//2: ]
    l2 = l2[::-1]
    number_list = l2+l1

    
    return number_list
     
number_list=[1,2,3,4,5,6]
print(exchange_list(number_list))
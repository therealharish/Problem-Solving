#lex_auth_01269446319507046499

def remove_duplicates(value):
    s=""
    for i in value:
        if(i in s):
            pass
        else:
            s+=i
    return s


print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
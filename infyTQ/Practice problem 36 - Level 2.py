#lex_auth_0127136518921830401222

def find_target_positions(input_string, target_word):
  ip = input_string
  tw = target_word
  d = {}
  l = ip.split(" ")
  for i in l:
    if(l in d):
      d[l].append(i)
    else:
      d[l] = [i]
  return d[tw]
  

def find_inverted_index(input_string):
  ip = input_string
  d = {}
  l = ip.split(" ")
  for i in l:
    if(l in d):
      d[l].append(i)
    else:
      d[l] = [i]


    
    return d
    
    
input_string="we dont need no education we dont need no thought control no we dont"
result_dict=find_inverted_index(input_string)
print(result_dict)
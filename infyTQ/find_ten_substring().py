#lex_auth_01269442545042227276

def find_ten_substring(num_str):
  l=[];
  for i in range(len(num_str)):
    s=num_str[i:];
    sum=0;
    index=0;
    for j in range(len(s)):
      while(sum<10 and j<len(s)):
        index=j;
        sum+=int(s[j])
        j+=1
      if(sum==10):
        l.append(s[:index+1])
        if(j!=(len(s)) and s[j+1]=='0'):
          l.append(s[:index+1]+"0")
      break;
  return l

num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
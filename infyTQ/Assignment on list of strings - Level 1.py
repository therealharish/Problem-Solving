#lex_auth_0127426166978887681375

def merge_list(list1, list2):
  merged_data=""
  i=0
  j = len(list2)-1
  while(i<len(list1) and j>-1):
    merged_data+=" "
    if(list1[i]):
      merged_data+=list1[i]
    if(list2[j]):
      merged_data+=list2[j]
      
    i+=1
    j-=1

  while(i<len(list1)):
    if(list1[i]):
      merged_data+=list1[i]
    i+=1

  while(j>-1):
    if(list2[j]):
      merged_data+=list2[j]
    j-=1
    
  return merged_data.strip(" ")

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)
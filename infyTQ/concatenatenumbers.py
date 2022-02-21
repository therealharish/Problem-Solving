def create_largest_number(number_list):
    l=number_list
    num1=str(l[0])+str(l[1])+str(l[2])
    num2=str(l[1])+str(l[2])+str(l[0])
    num1=str(l[2])+str(l[0])+str(l[1])

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
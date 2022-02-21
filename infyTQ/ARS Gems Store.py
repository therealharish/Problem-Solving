
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    if(len(reqd_gems)!=len(reqd_quantity)):
      return -1
    for i in range (len(reqd_quantity)):
      type = reqd_gems[i];
      num = reqd_quantity[i];
      try: 
        ind = gems_list.index(type)
      except Exception as e:
        return -1
      price = num*price_list[ind]
      bill_amount+=price;
    return bill_amount

price_list=[4392, 1342, 8734, 6421]
reqd_quantity=[2, 1, 3]
gems_list=['Amber', 'Aquamarine', 'Opal', 'Topaz']
reqd_gems=['Amber', 'Opal', 'Topaz']

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
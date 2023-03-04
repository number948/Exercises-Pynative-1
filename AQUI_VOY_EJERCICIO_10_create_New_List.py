def createNewList():
    list1 = [10, 20, 25, 30, 35]
    list2 = [40, 45, 60, 75, 90]
    odd_numbers = []
    for element in list1:
            if element % 2 != 0:
                odd_numbers.append(element)
                print(element)
    for element_y in list2:
            if element_y % 2 == 0:
                list3 = element_y
                print(list3, "\n ")

    new_list = odd_numbers.extend(list3)
    print(new_list)
               
   # ahora hay que juntar odd_numbers + list3, en ese orden , 
   


createNewList()
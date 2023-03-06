def createNewList():
    list1 = [10, 20, 25, 30, 35]
    list2 = [40, 45, 60, 75, 90]
   
    result_list = []
    
    for element in list1:
            if element % 2 != 0:
                result_list.append(element)

    for element_y in list2:
            if element_y % 2 == 0:
                result_list.append(element_y)
                
    print(result_list)
                  


createNewList()
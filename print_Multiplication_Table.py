def printMultiplicationTable():
    rows = 11
    columns = 11

    for i in range(1,rows):
        print()
        for j in range(1,columns):
           mult = i*j
           print(mult , end = " ")
    print("\t\t") 
printMultiplicationTable()
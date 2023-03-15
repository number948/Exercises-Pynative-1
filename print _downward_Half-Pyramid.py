def printDownwardHalfPyramid():
    cant = 5
    for i in range (6,0,-1):
        print()
        for j in range(0,i-1):
          print("*", end= " ")
    print()
     

printDownwardHalfPyramid()
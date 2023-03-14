def extractItemInReverseOrder():
    number = 7536

    while number != 0:
        digit = number % 10
        #print("digit", digit)
        number = number // 10
        
        print(digit, end ="")

extractItemInReverseOrder()
def sumCurrentPreviousNumber():
    sum = 0
    a = 0
    for i in range(0, 10):
        a = i -1
        if a < 1:
            a = 0
        sum = i + a
        print("numero actual: ",i,"numero anterior: ", a,
               "suma de ambos numeros: ", sum)
    
    return

sumCurrentPreviousNumber()


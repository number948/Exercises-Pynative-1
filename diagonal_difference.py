def diagonalDifference(arr):
    #print(matriz)
    diagonal_1 = 0
    diagonal_2 = 0
    
    for i in range (len(arr)):
        for j in range(len(arr)):
            if i == j:
                diagonal_1+=arr[i][j]
            if j==len(arr)-i-1:
                diagonal_2+=arr[i][j]
         
    diferencia = abs(diagonal_1 - diagonal_2)
    return diferencia


matriz_ejemplo = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(matriz_ejemplo))
                                     
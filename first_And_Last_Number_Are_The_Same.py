def firstAndLastNumberAreTheSame(numbers_x):
    numbers_inicio = numbers_x[0]
    numbers_final = numbers_x[-1] #aqui ya te da la posicion entnces en el if solo comparas las variables
   
    if numbers_inicio == numbers_final:
        return True
    else:
        return False
    

        
#respuesta pagina

def first_last_same(numberList):
    print("Given list:", numberList)
    
    first_num = numberList[0]
    last_num = numberList[-1]
    #print(last_num)
    
    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))

print(firstAndLastNumberAreTheSame([10, 20, 30, 40, 10]))
print(firstAndLastNumberAreTheSame([75, 65, 35, 75, 30]))
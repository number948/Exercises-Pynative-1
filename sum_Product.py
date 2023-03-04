
def sumProduct(number_1, number_2):  
    product = number_1 * number_2
    sum = number_1 + number_2

    if product <= 1000:
        return product
    else:
        return sum

resultado = sumProduct(20 ,30)
print("el resultado es:", resultado)
resultado = sumProduct(40, 30)
print("el resultado es:", resultado)

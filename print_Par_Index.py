def print_par_index():
    print("Ingrese la cadena")
    str = input()
    
    for index in range(len(str)):
       if index %2 == 0:
        print(str[index])

print_par_index()
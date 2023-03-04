def removeCaractersFromString(str, num):
    list_1 = list(str) #transforma un string en una lista (las listas son modificables)
    caracteres_a_eliminar = list_1[0:num] #("selecciono" los "n" caracteres que deseo eliminar del strig, que aun es lista)
    str2 = "".join(caracteres_a_eliminar) #transformo lista caracteres_eliminados a string, como pedia el ejercicio
    new_str3 = str.replace(str2, "" ) #usando la propiedad de string, replace, reemplazo en el string new_str2 los caracteres dentro de str2 con un espacios equivalentes a los caracteres dentro de str2 
    print("cadena original: ", str)
    return new_str3
    
#para que "imprima" lo qu pones en return debes como llamar a la funcion dentro de un print

print(removeCaractersFromString("pynative", 5))

#la actual solución era:

def remove_chars(word, n):
        
    print('Original string:', word)
    x = word[n:]
    return x

print(remove_chars("pynation", 2))
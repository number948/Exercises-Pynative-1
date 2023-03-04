def printPattern():
    #se necesitó de dos loops uno para crear las columnas y otro para imprimir las repeticiones
    columnas = 5
    for elemento in range(columnas +1):
        for i in range(elemento):
            print(elemento, end=" ")
        print("") 

printPattern()
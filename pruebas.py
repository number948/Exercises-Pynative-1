def calculate (num1, num2=4):
  res = num1 * num2
  print(res)

calculate(5, 6)

listOne = [20, 40, 60, 80]
listTwo = [20, 40, 60, 80]

print(listOne == listTwo)
print(listOne is listTwo)



for i in range(1, 5):
    print(i)
else:
    print("this is else block statement" )

var = "James" * 2  * 3
print(var)


salary = 8000

def printSalary():
  salary = 12000
  print("Salary:", salary)
  
printSalary()
print("Salary:", salary)

x = 36 / 4 * (3 +  2) * 4 + 2
print(x)

var= "James Bond"
print(var[2::-1]) # hasta la posicion 2  invertir el texto

p, q, r = 10, 20 ,30
print(p, q, r)

str = "pynative"
print (str[1:3])  #imprime lo que esta dentro de esos numeros sin llegar al final que seria el 3


sampleSet = {"Jodi", "Eric", "Garry"}
sampleSet.add("Vicki")
print(sampleSet)
def checkPalindrome(number):
    reverse = number[::-1]
    print(reverse)
    if number == reverse:
        print("Yes. given number is palindrome number")
    else:
        print("No. given number is not palindrome number")
#buscar otra forma de hacer reverse a un numero, creo que 

checkPalindrome("121")
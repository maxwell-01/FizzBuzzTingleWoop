def oldreplacer(number1, number2, word1, word2):
    num1 = int(number1)
    num2 = int(number2)
    for i in range(0,101,1):
        if i%num1 == 0 and i%num2 == 0:
            print(word1+word2)
        elif i%num1 == 0 and i%num2 > 0:
            print(word1)
        elif i%num1 > 0 and i%num2 == 0:
            print(word2)
        else:
            print(i)

# oldreplacer(3,5,"Fizz","Buzz")
# oldreplacer(3,14,"Tingle","Woop")

def divisible(number1, number2):
    num1 = int(number1)
    num2 = int(number2)
    #Checks if num2 fits perfectly inside number1
    if num1%num2 > 0:
        return False
    else:
        return True

def replacer(number1, number2, word1, word2):
    num1 = int(number1)
    num2 = int(number2)
    for i in range(0,101,1):
        if divisible(i,num1) and divisible(i,num2):
            print(word1+word2)
        elif divisible(i,num1) and not divisible(i,num2):
            print(word1)
        elif not divisible(i,num1) and divisible(i,num2):
            print(word2)    
        else:
            print(i)
replacer(3, 5, "Fizz", "Buzz")

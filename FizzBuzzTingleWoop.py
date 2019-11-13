for i, j in range(0,101,1), range(0,101,1):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0 and i%5 > 0:
        print("Fizz")
    elif i%3 > 0 and i%5 == 0:
        print("Buzz")
    elif i%3> 0 and i%5 > 0:
        print(i)
    elif j%3 == 0 and j%14 == 0:
        print("TingleWoop")
    elif j%3 == 0 and j%14 > 0:
        print("Tingle")
    elif j%3 > 0 and j%14 == 0:
        print("Woop")
    else:
        print(j)


# for i, j in range(1, 6 + 1), range(10, 5, -1):

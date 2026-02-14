# Exercise 5: Factorial function

def factorial(n):
    if n == 0:
        return f"{n}! = 1."
    else :
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return f"{n}! = {fact}"

while True:      
    n = input("enter a number: ")
    try:
        n = int(n)
        if n < 0:
            n = int(input("enter a (positive) number : "))
            continue

        print(factorial(n))
        break
    except:
        print('enter a valid number')

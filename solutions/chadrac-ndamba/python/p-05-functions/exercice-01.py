# Exercise 1: Add Two Numbers with Function

def add(a,b):
    return a + b

while True:
    a = input("enter a:")
    b = input("enter b:")
    try:
        a , b = int(a) , int(b)
        
        result = add(a,b)
        print(f'{a} + {b} = {result}')
        break
    except ValueError:
        print("enter valid numbers (integer)")
    

# Exercise 1: Even or Odd

while True:
    n = input('Enter a number :')
    try:
        n = int(n)
        if n % 2 == 0:
            print('Even')
            break
        else:
            print('Odd')
            break
    except:
        print('error ! you have to enter an integer.')
        

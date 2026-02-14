while True:
    n = input('enter a number:')
    try: 
        n = int(n)
        while n < 0:
            n = int(input('enter a number (enter a positive number):'))
            continue

        sum = 0
        for i in range(1 , n + 1):
            sum += i
            
        print(sum) 
        break 
    except:
        print("error ! (enter an integer)")
    

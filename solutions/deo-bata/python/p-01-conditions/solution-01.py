while True:
    try:
        n = int(input("Please enter a valid number: "))        
        break
    except:
        print("N has to be an integer")


if n % 2 == 0:
    print("Even")
else:
    print("Odd")


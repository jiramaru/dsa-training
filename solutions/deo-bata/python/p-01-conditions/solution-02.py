year = 0

while year < 1000:
    try:
        year = int(input("Please enter a valid year: "))
        if year < 1000:
            print("Year must be greater than 1000")
    
    except:
        print("Year has to be a valid integer")


if (year % 4 == 0 and year % 100 !=0 ) or year % 400 == 0:
    print("Leap")
else:
    print("Not leap")
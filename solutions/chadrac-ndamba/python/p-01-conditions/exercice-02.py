# Exercise 2: Leap Year (Bixextile Year)
while True:
    year =input('Enter a year:') 
    
    try:
        year = int(year)
        if year <=0:
            print('enter a valid year !')
            continue
    
        if (year % 4 == 0 and year % 100 !=0 ) or year % 400 == 0:
            print("Leap")
            break
        else:
            print("Not leap")
            break
    except ValueError:
        print('enter a valid year please ! (an integer)')
        
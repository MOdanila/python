'''
The user types in a number from 1 to 7 that represents a day of the week. Print its name. 
For example, if the number is 1, then you should display "Monday"; if 2, display "Tuesday," etc.
'''
day = int(input("Enter a number from 1 to 7: "))

if day == 1:
    day_name = "Monday"
elif day == 2:
    day_name = "Tuesday"
elif day == 3:
    day_name = "Wednesday"
elif day == 4:
    day_name = "Thursday"
elif day == 5:
    day_name = "Friday"
elif day == 6:
    day_name = "Saturday"
elif day == 7:
    day_name = "Sunday"
else:
    day_name = "Invalid day"

print(day_name)


'''
The user types in a number from 1 to 12 that represents a month. Print its name. 
For example, if the number is 1, display "January"; if 2, display "February," etc.
'''
month = int(input("Enter a number from 1 to 12: "))

if month == 1:
    month_name = "January"
elif month == 2:
    month_name = "February"
elif month == 3:
    month_name = "March"
elif month == 4:
    month_name = "April"
elif month == 5:
    month_name = "May"
elif month == 6:
    month_name = "June"
elif month == 7:
    month_name = "July"
elif month == 8:
    month_name = "August"
elif month == 9:
    month_name = "September"
elif month == 10:
    month_name = "October"
elif month == 11:
    month_name = "November"
elif month == 12:
    month_name = "December"
else:
    month_name = "Invalid month"

print(month_name)


'''
The user types in a number. If the number is greater than 0, print "Your number is positive"; 
if it is less than zero, print "Your number is negative"; if it is equal to 0, 
print "Your number is equal to zero."
'''
number = int(input("Enter a number: "))
print("Your number is positive" if number > 0 else "Your number is negative" if number < 0 else "Your number is equal to zero") 


'''
The user types in two numbers.Determine if these numbers are equal. 
If they are not, print them in ascending order.
'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 != num2:
    if num1 > num2:
        print(num2, num1)
    else:
        print(num1, num2)
else:
    print("The numbers are equal")
    
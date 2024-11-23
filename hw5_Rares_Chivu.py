'''
The user types in two numbers (start and end points of the range). Analyze all the numbers in this 
range as follows: if the number is a multiple of 7, print it.
'''
def analyze_range(start, end):
    for i in range(start, end + 1):
        if i % 7 == 0:
            print(i)

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
analyze_range(start, end)


'''
The user types in two numbers (start and end points of the range). 
Analyze all the numbers in this range. Print the following:
All numbers in the range;
All numbers in the range in descending order;
All numbers that are multiples of 7;
How many numbers are multiples of 5.
'''

def analyze_range(start, end):
    print("All numbers in the range:")
    for i in range(start, end + 1):
        print(i, end=' ')
    print("\nAll numbers in the range in descending order:")
    for i in range(end, start - 1, -1):
        print(i, end=' ')
    print("\nAll numbers that are multiples of 7:")
    for i in range(start, end + 1):
        if i % 7 == 0:
            print(i, end=' ')
    print("\nHow many numbers are multiples of 5:")
    count = 0
    for i in range(start, end + 1):
        if i % 5 == 0:
            count += 1
    print(count)

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
analyze_range(start, end)


'''
The user types in two numbers (start and end points of the range). Analyze all the 
numbers in this range. The output should be according to the rules specified below.

If the number is a multiple of 3 (divisible by 3 without remainder), print the word 
Fizz. If it is a multiple of 5, print Buzz. If it is a multiple of 3 and 5, print 
Fizz Buzz. If the number is not a multiple of 3 or 5, print the number itself.
'''
def analyze_range(start, end):
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
analyze_range(start, end)
'''
Task 1
The user types in two numbers. Print all the numbers in the specified range.

Task 2
The user types in two numbers. Print all odd numbers in the specified range.

Task 3
The user types in two numbers. Print all even numbers in the specified range.

Task 4
The user types in two numbers. Print all numbers in the specified range in descending order.

Task 5
The user types in two numbers. Print all odd numbers in the specified 
range. If the end and start points of the range are incorrect, normalize 
them. Let's say the user typed in 33 and 13, normalization will assign 
13 to the start and 33 to the end of the range.
'''

# Task 1
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
for i in range(start, end + 1):
    print(i, end=' ')
    
# Task 2
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
for i in range(start, end + 1):
    if i % 2 != 0:
        print(i, end=' ')
    
# Task 3
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i, end=' ')
    
# Task 4
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
for i in range(end, start - 1, -1):
    print(i, end=' ')
    
# Task 5
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
if start > end:
    start, end = end, start
for i in range(start, end + 1):
    if i % 2 != 0:
        print(i, end=' ')
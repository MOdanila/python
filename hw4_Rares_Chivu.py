'''
Print the multiplication table for the user-defined number.
'''
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}\n")

'''
Write a currency converter program. Implement a dialog with the user through a 
menu. The user types in a number and the program prints the number 
in different currencies.
'''   
def currency_converter():
    print("Currency Converter")
    print("1. USD to EUR")
    print("2. USD to JPY")
    print("3. USD to GBP")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        usd = float(input("Enter USD: "))
        eur = usd * 0.88
        print(f"{usd} USD is equal to {eur} EUR")
    elif choice == "2":
        usd = float(input("Enter USD: "))
        jpy = usd * 110
        print(f"{usd} USD is equal to {jpy} JPY")
    elif choice == "3":
        usd = float(input("Enter USD: "))
        gbp = usd * 0.75
        print(f"{usd} USD is equal to {gbp} GBP")
    elif choice == "4":
        print("Exiting...")
    else:
        print("Invalid choice. Please try again.")

while True:
    currency_converter()
    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower() != "yes":
        break


'''
The user types in the start and end points of the range and a number. 
If the number is not in the range, the program asks the user to re-enter the number,
and so on until the user enters the number correctly. 
The program displays all numbers in the range, highlighting the number with 
exclamation marks. For instance: 1 2 3 !4! 5 6 7.
'''    
def range_checker():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    number = int(input("Enter a number: "))
    while number < start or number > end:
        number = int(input("Enter a number in the range: "))
    for i in range(start, end + 1):
        if i == number:
            print(f"!{i}!", end=" ")
        else:
            print(i, end=" ")

range_checker()


'''
Develop a game Guess the Number. The program chooses a number in the range 
from 1 to 500. The user tries to guess it. After each try, the program gives 
hints on whether the number is greater or less than the guessed number. 
In the end, the program displays statistics: how many tries it took to guess 
the number, how long it took. Provide an exit by entering 0 if the user is 
tired of guessing the number.
'''
import random
import time
def guess_the_number():
    start_time = time.time()
    number = random.randint(1, 500)
    attempts = 0
    while True:
        guess = int(input("Enter a number: "))
        attempts += 1
        if guess == number:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Congratulations! You guessed the number in {attempts} attempts and it took {elapsed_time:.2f} seconds.")
            break
        elif guess < number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
        if guess == 0:
            print("You gave up. The number was", number)
            break

guess_the_number()

    

        
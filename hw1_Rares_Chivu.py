'''
The user types in a number from 1 to 100. If the number is a multiple of 3 (divisible by 3 without remainder), print the word Fizz. 
If the number is a multiple of 5, print the wordBuzz. 
If the word is a multiple of 3 and 5, print Fizz Buzz. 
If the word is not a multiple of 3 and 5, print the number.
If the user typed in a number out of the range, print an error message.
'''

a=int(input("Enter a number between  1 and 100: "))
if(a>=1 and a<=100):
    if(a%3==0  and a%5==0):
        print("FizzBuzz")
    elif(a%3==0):
        print("Fizz")
    elif(a%5==0):
        print("Buzz")
else:
    print("Error: Number out of range")
    


'''
Write a program that, at the user's choice, raises 
the typed in number to the power of 0 through 7.
'''
def  power(n, p):
    return n ** p

a = int(input("Enter the number you want to raise: "))
b = int(input("Enter the power you want to raise the number to: 0-7"))
if(b>=0 and b<=7):
    print(power(a,b))
else:
    print("Power out of range. Please enter a power between 0 and 7.")


'''
Write a program that calculates the cost of a call 
for different mobile phone operators. The user types 
in the cost of the call and chooses operators for 
the outgoing and incoming calls. Print the cost.
'''
operator_rates = {
    'Operator A': 0.10,  
    'Operator B': 0.15,  
    'Operator C': 0.20  
}

def calculate_call_cost(call_cost, outgoing_operator, incoming_operator):
    
    outgoing_rate = operator_rates[outgoing_operator]
    incoming_rate = operator_rates[incoming_operator]

    total_cost = call_cost + (call_cost * outgoing_rate) + (call_cost * incoming_rate)
    return total_cost

def main():
    call_cost = float(input("Enter the cost of the call: "))

    print("Choose outgoing operator: ")
    print("Operator A")
    print("Operator B")
    print("Operator C")
    outgoing_operator = input("Enter outgoing operator: ")

    print("Choose incoming operator: ")
    print("Operator A")
    print("Operator B")
    print("Operator C")
    incoming_operator = input("Enter incoming operator: ")

    final_cost = calculate_call_cost(call_cost, outgoing_operator, incoming_operator)
    print("The total cost of the call is: $", round(final_cost, 2))

main()


'''
The salary of a salesperson is $200 + percentage of sales as 
follows: up to $500 — 3%, from 500 to 1000 — 5%, over 1000 — 8%.
The user types in the sales for three salespersons. 
Determine their salary, the best salesperson, give him or her 
a $200 bonus, print the result.
'''
def calculate_salary(sales):
    base_salary = 200
    if sales <= 500:
        commission = sales * 0.03
    elif sales <= 1000:
        commission = sales * 0.05
    else:
        commission = sales * 0.08
    
    total_salary = base_salary + commission
    return total_salary

def main():
    salespersons = []
    salaries = []

    for i in range(3):
        sales = float(input(f"Enter sales for salesperson {i + 1}: "))
        salary = calculate_salary(sales)
        salespersons.append(sales)
        salaries.append(salary)

    best_index = salaries.index(max(salaries))
    best_salary = salaries[best_index] + 200  

    for i in range(3):
        print(f"Salary for salesperson {i + 1}: ${salaries[i]:.2f}")

    print(f"Best salesperson is salesperson {best_index + 1} with a total salary of: ${best_salary:.2f}")

if __name__ == "__main__":
    main()
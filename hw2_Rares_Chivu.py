'''
The user types in the time in seconds since the beginning of the day. 
Based on the user's choice, calculate how many hours, minutes, and seconds 
are left until midnight.
'''
def calculate_time_left(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return hours, minutes, seconds

seconds = int(input("Enter the number of seconds since midnight: "))

hours, minutes, seconds = calculate_time_left(seconds)

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

'''
The user types in the diameter of a circle. Based on the user's choice, 
calculate the area or perimeter of the circle.
'''
import math
def calculate_circle_properties(diameter):
    radius = diameter / 2
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter

diameter = int(input("Enter the diameter of the circle: "))

area, perimeter = calculate_circle_properties(diameter)

print("Area:", area)


'''
The user types in the cost of one gaming console, their quantity, 
and a discount. Based on the user's choice, calculate the total 
amount of the order or the cost of one console, including the discount.
'''
def calculate_order_cost(console_cost, quantity, discount):
    total_cost = console_cost * quantity
    discount_amount = total_cost * (discount/100)
    total_cost -= discount_amount
    return total_cost

console_cost = float(input("Enter the cost of one gaming console: "))
quantity = int(input("Enter the quantity of the console: "))
discount = float(input("Enter the discount: "))

final_cost = calculate_order_cost(console_cost, quantity, discount)
print("The total cost of the order is: $", round(final_cost, 2))


'''
The user types in the file size in gigabytes and the bandwidth in bits 
per second. Based on the user's choice, calculate how many hours, 
or minutes, or seconds it will take to download a file.
'''
def calculate_download_time():
    file_size_gb = int(input("Enter the file size in GB: "))
    bandwidth_bps = int(input("Enter the bandwidth in bits per second: "))

    file_size_bytes = file_size_gb * 1024 * 1024 * 1024 

    download_time_seconds = file_size_bytes / bandwidth_bps

    hours = int(download_time_seconds // 3600)
    minutes = int((download_time_seconds % 3600) // 60)
    seconds = int(download_time_seconds % 60)
 
    if hours > 0:
        print(f"The download will take {hours} hours, {minutes} minutes, and {seconds} seconds.")
    elif minutes > 0:
        print(f"The download will take {minutes} minutes and {seconds} seconds.")
    else:
        print(f"The download will take {seconds} seconds.")

calculate_download_time()


'''
The user types in an hour (from 0 to 23). If the received value is in 
the range from 0 to 6, print Good Night; if from 6 to 13, print 
Good Morning; if from 13 to 17, print Good Day; if from 17 to 0, 
print Good Evening. The upper limit of the range is not included. 
For instance, if 6 is typed in, 6 belongs to the range from 6 to 13.
'''
def calculate_time_of_day():
    hour = int(input("Enter an hour: "))

    if hour >= 0 and hour < 6:
        print("Good Night")
    elif hour >= 6 and hour < 13:
        print("Good Morning")
    elif hour >= 13 and hour < 17:
        print("Good Day")
    elif hour >= 17 and hour < 24:
        print("Good Evening")
    else:
        print("Error: Invalid hour")

calculate_time_of_day()

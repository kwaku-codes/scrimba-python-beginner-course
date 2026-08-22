# Challenge: Build a simple paycheck calculator.
# 1. Instead of hard coded values, prompt the user for their hourly_rate and hours_worked. 
# 2. Convert hourly_rate to a float and hours_worked to an integer.
# 3. Type check both variables.
# 4. Multiply them together and print the total pay.

hourly_rate = float(input("What is your hourly rate? "))
print (hourly_rate) 
print(type(hourly_rate))

hours_worked = int(input("How many hours did you work this week? "))
print(hours_worked)
print(type(hours_worked))

total_pay = (hourly_rate * hours_worked)
print(f"Your total pay for the week is £{total_pay} congratulations enjoy payday")

# Challenge: Gather Input from Users
# This challenge is to highlight your skill of the input() Python. 

# We need four things from the user:

# - The name of the event or occasion
# - The cost
# - The tip or service charge
# - How many people are splitting the bill

# 1. Replace the hardcoded values for event, cost, service_charge, and group_size with input() prompts.
# 2. Keep grand_total and total_per_person hardcoded for now. They won't be entered by the user.
# 3. Run the program and make sure your prompts are clear and the display looks right.

# input("Service charge? ") 
# input("Was there a tip or a service charge? Enter a whole number (e.g. 20 for 20%: ")

#PayUp App First Iteration 

# event = input("What is the name of the event you want to split the bill for? ")
# cost = float(input("How much did the event cost? "))
# service_charge =int(input("Was there a tip or a service charge? Enter a whole number (e.g. 20 for 20%: "))
# group_size = int(input("How many people attended? "))
# grand_total = 330
# total_per_person = 110

# print("Welcome to PayUp!")
# print()
# print(f"Here's the breakdown for {event}:")
# print()
# print(f"Cost: ${cost}")
# print()
# print(f"Service charges: ${service_charge}")
# print()
# print(f"Group size: {group_size}")
# print(f"Grand total: ${grand_total}")
# print()
# print(f"Each person must PayUp: ${total_per_person}")

# print(type(cost))
# print(type(service_charge)) 
# print(type(group_size))

#=========================== CHALLENGE CONTINUES ========================================================
# Challenge: Calculate the Split
#
# 1. Calculate service_charge_total. The user enters a whole number percentage,
#    so you'll need to convert it to a decimal and multiply it by cost to get the dollar amount.
#    Save the result to service_charge_total. Check the hints.md file if you're unsure about the math!
#
# 2. Add cost and service_charge_total to get the grand total.
#    Save it to grand_total.
# 3. Divide grand_total by group_size to get total_per_person.

event = input("What is the name of the event you want to split the bill for? ")
cost = float(input("How much did the event cost? "))
service_charge =int(input("Was there a tip or a service charge? Enter a whole number (e.g. 20 for 20%: "))

service_charge_total = cost * service_charge / 100

group_size = int(input("How many people attended? "))
grand_total = cost + service_charge_total 
total_per_person = grand_total / group_size

print("Welcome to PayUp!")
print()
print(f"Here's the breakdown for {event}:")
print()
print(f"Cost: ${cost}")
print()
print(f"Service charges: ${service_charge_total}")
print()
print(f"Group size: {group_size}")
print(f"Grand total: ${grand_total}")
print()
print(f"Each person must PayUp: ${total_per_person}")
print()
print(type(cost))
print(type(service_charge)) 
print(type(group_size))
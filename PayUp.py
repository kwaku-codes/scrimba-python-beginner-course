# Challenge: Create the output display for the PayUp app.

# 1. Check out the example output in `example_output.md`
# 2. Define a variable for each item: event name, cost, service charge,
#    group size, grand total, and total per person. Use made-up values for now —
#    we'll do the math later!
# 3. Build the display line by line using print() and f-strings. 
#    Remember: an empty print() creates a blank line.
# 4. Run it and make sure it matches the example

event_name = "Birthday Party"
cost = "$100"
service_charge = "$10"
group_size = 5
grand_total = "$110"
total_per_person = "$22"

print(f"Welcome to PayUp!") 
print() 
print(f"Here's the breakdown for {event_name} at All Bar One")
print() 
print(f"Cost: {cost}")
print(f"Service Charge: {service_charge}")
print(f"Group Size: {group_size}")
print(f"Grand Total: {grand_total}")
print() 
print(f" Each person must PayUp: {total_per_person}") 

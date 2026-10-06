# Challenge: Build a Support Queue
# You're building a help desk feature that shows who's waiting
# in line for support.

# Use indexing to print a status display that looks like this:
#
#   Now helping: Ada
#   Next in line: Grace
#   Just added: Alan
#
# "Now helping" is the first person in line, "Next in line" is second, and "Just added" is the last person in the queue.


tickets = ["Ada", "Grace", "Linus", "Margaret", "Alan"]

# Ada = 0 
# Grace = 1
# Linus = 2 
# Margaret = 3
# Alan = 4

now_helping = tickets[0]
next_in_line = tickets[1]
just_added = tickets[2]

print(f"You are in the following position in the helpdesk queue") 
print(f"Now helping: {now_helping}")
print(f"Next in line is: {next_in_line}")
print(f"And just added is: {just_added} last in the queue")



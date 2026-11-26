# This challenge is meant to demonstrate how to use the equality operator to define a value as true or false
# Additionally it also introduces the concept of Booleans 

promo_code = "FLASH50"

user_code = input("Enter your promo code: ")

print(promo_code == user_code)
print(promo_code != user_code)


# If a user enters the string promo code differently from how it is displayed in the variable it will return fasle
# This is because the equals operator is case sensitive 
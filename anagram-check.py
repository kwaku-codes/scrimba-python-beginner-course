# Challenge: Anagram Check
# Anagrams are two words made from the exact same letters rearranged,
# like "listen" and "silent".

# For each pair below, split both words into lists, sort them, and print
# the results. If the two lists match, the words are anagrams.

# 1. "earth" and "heart"
# 2. "below" and "elbow"
# 3. "night" and "tight"

#Below is my code to solve the challenge

first_word = list("earth")
second_word = list("heart")
third_word = list ("below")
fourth_word = list ("elbow") 
fifth_word = list ("night")
sixth_word = list ("tight") 

print(sorted(first_word))
print(sorted(second_word))
print(sorted(third_word))
print(sorted(fourth_word))
print(sorted(fifth_word))
print(sorted(sixth_word))
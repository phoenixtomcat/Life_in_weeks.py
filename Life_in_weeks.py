# Prompt the user to input their age
age = input("Input your age: ")

# Calculate how many weeks they have left if they live until 90. 52 weeks in a year.
age_difference = 90 - int(age)
weeks_left = age_difference * 52

# Print out how many weeks they have left.
print(f"You have {weeks_left} weeks left.")
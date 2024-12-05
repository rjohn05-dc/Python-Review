# 1. String Manipulation
word=input("Enter a string")

print("Uppercase" + word.upper())
print("Lowercase" + word.lower())
print("Reversed" + word[::-1])
print("VowelReplacement" + word.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*"))

# 2. Math Operators
num=float(input("Enter the first number"))
num2=float(input("Enter the second number"))

res=num + num2
print(res)

res2=num - num2
print(res2)

res3=num * num2
print(res3)

res4=num / num2
print(res4)

res5=num % num2
print(res5)

res6=num ** num2
print(res6)


# 3 Concatenation
# Ask the user for their first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenate the names into a full name
full_name = first_name + " " + last_name

# Print a greeting message
print(f"Hello, {full_name}!")

# Ask for the user's favorite number
favorite_number = input("Enter your favorite number: ")

# Append the favorite number to the full name
modified_name = full_name + favorite_number

# Print the modified full name
print(f"Your modified name: {modified_name}")


# 4 Function
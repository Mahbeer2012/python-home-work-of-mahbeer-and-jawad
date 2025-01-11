# Calculate the square root without conditions or imports

# Input from the user

number = float(input("Enter a number to calculate its square root: "))

# Calculate the square root

sqrt = (number if number >= 0 else -number) ** 0.5

# Display the result

print(f"The square root of {number} is {sqrt}")
# Progect to check ascii value of a given character

# input from the user
chracter = input("enter a chracter:")

# encure the input is a single chracter
if len(chracter) == 1:
    # get the ascii value
    ascii_value = ord(chracter)
    print(f"the ASCII value of'{chracter}'is{ascii_value}.")
else:
    print("please enter a valid chracter")
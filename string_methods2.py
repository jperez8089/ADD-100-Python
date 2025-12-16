# Python String Methods Practice

# TODO: Use the capitalize() method to capitalize the first letter of the string
# Example: "python" -> "Python"
string1 = "python"
result1 = string1.capitalize()
print(result1)

# TODO: Use the center() method to center the string in a string of specified width
# Example: "python" -> " python "
string2 = "python"
x = string2.center(25)
print(x)

# TODO: Use the endswith() method to check if the string ends with a specified substring
# Example: Check if "python" ends with "on"
string3 = "python"
x = string3.endswith("on")
print(x)

# TODO: Use the find() method to find the first occurrence of a substring in the string
# Example: Find the position of "th" in "python"
string4 = "python"
x = string4.find("th")
print(x)

# TODO: Use the isalnum() method to check if all characters in the string are alphanumeric
# Example: Check if "python3" is alphanumeric
string5 = "python3"
x = string5.isalnum()
print(x)

# TODO: Use the isalpha() method to check if all characters in the string are alphabetic
# Example: Check if "python" is alphabetic
string6 = "python"
x = string6.isalpha()
print(x)

# TODO: Use the islower() method to check if all characters in the string are lowercase
# Example: Check if "python" is in lowercase
string7 = "python"
x = string7.islower()
print(x)

# TODO: Use the isspace() method to check if all characters in the string are whitespaces
# Example: Check if " " is all whitespace
string8 = " "
x = string8.isspace()
print(x)

# TODO: Use the isupper() method to check if all characters in the string are uppercase
# Example: Check if "PYTHON" is in uppercase
string9 = "PYTHON"
x = string9.isupper()
print(x)

# TODO: Use the join() method to join elements of an iterable with the string as the separator
# Example: Join ["Python", "is", "fun"] with "-" as separator
iterable1 = ["Python", "is", "fun"]
separator = "-"
x = separator.join(iterable1)
print(x)

# TODO: Use the lower() method to convert all characters in the string to lowercase
# Example: Convert "PYTHON" to lowercase
string10 = "PYTHON"
x = string10.lower()
print(x)

# TODO: Use the lstrip() method to remove leading characters (spaces by default)
# Example: Remove leading spaces from " python"
string11 = " python"
x = string11.lstrip()
print("testing the string", x)


# TODO: Use the rstrip() method to remove trailing characters (spaces by default)
# Example: Remove trailing spaces from "python "
string12 = "python "
x = string12.rstrip()
print(x)

# TODO: Use the replace() method to replace all occurrences of a substring with another substring
# Example: Replace "python" with "snake" in "I love python"
string13 = "I love python"
x = string13.replace("python", "snake")
print(x)

# TODO: Use the rfind() method to find the highest index of a substring
# Example: Find the highest index of "n" in "python"
string14 = "python"
x = string14.rfind("n")
print(x)

# TODO: Use the split() method to split the string at a specified separator
# Example: Split "python-is-fun" at "-"
string15 = "python-is-fun"
result16 = string15.split("-")
print(result16)

# TODO: Use the startswith() method to check if the string starts with a specified substring
# Example: Check if "python" starts with "py"
string16 = "python"
x = string16.startswith("py")
print(x)

# TODO: Use the strip() method to remove both leading and trailing characters (spaces by default)
# Example: Remove spaces from " python "
string17 = " python "
x= string17.strip()
print(x)

# TODO: Use the swapcase() method to swap the case of all characters in the string
# Example: Swap case of "Python"
string18 = "Python"
x = string18.swapcase()
print(x)

# TODO: Use the title() method to convert the first character of each word to uppercase
# Example: Convert "python is fun" to title case
string19 = "python is fun"
x = string19.title()
print(x)

# TODO: Use the upper() method to convert all characters in the string to uppercase
# Example: Convert "python" to uppercase
string20 = "python"
x = string20.upper()
print(x)
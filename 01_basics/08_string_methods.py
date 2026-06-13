# --------------------------------- String Methods -----------------------------------------
name = input("Enter your full name: ")

# length
length = len(name)

print(length)

# first occurence
result =name.find("A")    # the find method will return the first occurence of a given character , the position
print(result)

# last occcurence
result = name.rfind("o")     # If python is not able to locate a given character it will return negative one (-1)
print(result)

# This method turns only the very first character of the
# entire string into uppercase. Everything else in the string is forced into lowercase.
result = name.capitalize()
print(result)

# This method turns the first letter of every
# single word into uppercase, and makes the rest of the letters in those words lowercase.
result = name.title()
print(result)

# upper method will take all characters in a string and make it upper case
result = name.upper()
print(result)

# lower method will take all characters in a string and make it lower case
result = name.lower()
print(result)

# isdigit method will return either true or false if , true if there are only digits in that string else false
result = name.isdigit()
print(result)

# isalpha method will return either true or false if , true if there are only alphabetical character in that string else false
result = name.isalpha()                       # remember space is not an alphabetical character
print(result)

# isalnum method will return True if all characters in the string are alphanumeric, otherwise it will return False
result = name.isalnum()
print(result)

phone_number = input("Enter you phone number #:")

# let's check how many characters (here we are checking dashes) in our string
result = phone_number.count("-")
print(result)

# replace method replaces any occurence with one character with another, it's most useful method of string
result = phone_number.replace("-"," ")    # We can also eliminate dashes or another character by replacing it with
print(result)                                          # empty string  like this  phone_number.replace("-","")


# Only removes spaces at the start and end
text = "  yes  "
clean_text = text.strip()
print(clean_text)  # Output: "yes"

# Removes only leading whitespace (spaces at the start of the string).
text = "  yes  "
print(text.lstrip())  # Output: "yes  "


# Removes only trailing whitespace (spaces at the end of the string).
text = "  yes  "
print(text.rstrip())  # Output: "  yes"


# The .split() method splits a string into a list of smaller
# strings (called substrings) based on a separator. By default, it splits on whitespace.
text = "This is another example"
words = text.split()
print(words)


print(" ".join(["This","is","a","sentence"]))


test = "How-much-wood-would-a-woodchuck-chuck"
print(test.split("-"))         # prints ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']


print("-".join(test.split()))  # prints "How-much-wood-would-a-woodchuck-chuck"



# If you want to comprehensive list to all the string methods available to you
# print(help(str))


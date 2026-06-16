    # format specifiers = {value:flags} when used in the context of f-string, they allow
    #                      us to format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = Reserve a minimum width of that many characters.
# Python will never cut off the value if the value itself is longer.

# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ =   Always show the sign (+ or -)
# :  = insert a space before positive numbers
# :, = comma separator





price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price 1 is ${price1:.2f}") # it will display 2 decimal places
print(f"Price 2 is ${price2:.1f}") # it will display 1 decimal place
print(f"Price 3 is ${price3:.3f}") # it will display 3 decimal places

# to allocate space to display a value
# below each value has a total of 10 spaces to display the output
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")


# if you want to precede number with 0 , now these numbers will be 0 padded
print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")


# to left justify a number
print(f"Price 1 is ${price1:<10}")      # now we will have all space left after number
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

# to right justify a number
print(f"Price 1 is ${price1:>10}")      # now we will have all space left before number
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")

# Center align
print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")

# If you want to display a sign with a number
print(f"Price 1 is ${price1:+}")      # Positive numbers get a + sign
print(f"Price 2 is ${price2:+}")      # Negative numbers keep their - sign
print(f"Price 3 is ${price3:+}")

print(f"Price 1 is ${price1: }")  # Or Leave a blank space for positive numbers, but keep the - sign for negative numbers
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3: }")

# there is (1,000)thousand separator which is a comma
print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")

# We could also mix and match flags
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")

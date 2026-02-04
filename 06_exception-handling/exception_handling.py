# exception = an event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1. try   2. except  3. finally

# TypeError e.g., We type to perform an operation of a value that's of a wrong data type e.g.,
# print(1+"1")

# Value Errors tend to happen when you attempt to typecast the value of the wrong datatype
# int("Pizza")

# Exceptions will interrupt our program if they are not handled gracefully, here is how we can do that:

 # try:
 #     # Try some code, any code that's dangerous where it could cause an error, you will place it in a try block
 # e.g., any time you accept user input that is considered dangerous code because a user can, if exception happens
 # We will move to step 2
 # except Exception:
 #     # Handle an Exception
 # finally:
 #     # Do some clean up

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero!")                # Some people do is that they catch all exceptions
except Exception:
    print("Something went wrong!")
except ValueError:
    print("Enter only numbers please!")



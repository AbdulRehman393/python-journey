# exception = an event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1. try   2. except  3. finally

# TypeError e.g., We type to perform an operation of a value that's of a wrong data type e.g.,
# print(1+"1")

# Value Errors tend to happen when you attempt to typecast the value of the wrong datatype
# Value Error , when the value is not within an acceptable range.    e.g.,   float("hello)
# int("Pizza")

# Exceptions will interrupt our program if they are not handled gracefully, here is how we can do that:

 # try:
 #      Try some code, any code that's dangerous where it could cause an error, you will place it in a try block
 # e.g., any time you accept user input that is considered dangerous code because a user can, if exception happens
 # We will move to step 2
 # except Exception:
 #      Handle an Exception
 # finally:
 #      will always execute regardless there's an exception or not. Do some clean up such as if you're handling files
 # you may open a file , you want to be sure to close the file when you are done

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here")



# Some people do is that they catch all exceptions, This is considered bad practice,
# it's too broad it's good practice to tell the user what went wrong exactly.
# except Exception:
#    print("Something went wrong!")


#how to work with exceptions
#try, except, else, finally
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")
except TypeError:
    print("You can't add a string to an integer")
else:
    #this will run if there are no errors
    print("No errors")
finally:
    print("This will always run")
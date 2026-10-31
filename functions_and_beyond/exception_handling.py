# exception is kind of run-time problem
# Different types of exceptions: ValueError, ZeroDivisionError, KeyError
try:
    number = int(input("enter number: "))
    result = 100 / number
    print(result)

except ValueError:
    print("You must enter a number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print("You entered: ", number)    # run if successful

finally:
    print("Program Finished")    #run regardless
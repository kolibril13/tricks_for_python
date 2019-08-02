while True:
    try:
        x = int(input("Please enter a number: "))
        print("Cool")
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

'''
# Error types:
SyntaxError: invalid syntax

Exceptions: 
    * ZerodivisionError: division by zero
    * NameError: ...is not defined
    * TypeError; Can not convert...
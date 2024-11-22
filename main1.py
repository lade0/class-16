# try except finally(exception handling) handling
try:
    num1=int(input("enter your first number"))
    num2=int(input("enter your second number"))
    result=num1/num2
    print("result:",result)
except ZeroDivisionError:
    print("division by zero is not allowed")
except ValueError:
    print("plese enter a valid input")
except:
    print("some other error occurred")
finally:
    print("finally executes no matter what happens")
    

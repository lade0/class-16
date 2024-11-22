# value error
try:
    numb=int(input("enter a number"))
except ValueError as ex:
    print("exception:",ex)
# entering a number until it is even
valid=False
while not valid :
    try:
        m=int(input("enter a number"))
        while m%2==0:
            print("bye")
            valid=True
    except ValueError:
        print("invalid")
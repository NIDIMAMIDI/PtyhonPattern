try:
    n1 = int(input("Enter a First number :"))
    n2 = int(input("Enter second number: "))
    n3 = int(input("Enter third number: "))
except ValueError :
    print("Enter only integers as input")
if n1 > n2:
    if n1 > n3:
        print(n1, "is Greatest")
    else:
        print(n3, "is Greatest")
else:
    if n2 > n3:
        print(n2, "is Greatest")
    else:
        print(n3, "is Greatest")
if n1 < n2:
    if n1 < n3:
        print(n1, "is Smallest")
    else:
        print(n3, "is Smallest")
else:
    if n2 < n3:
        print(n2, "is Smallest")
    else:
        print(n3, "is Smallest")

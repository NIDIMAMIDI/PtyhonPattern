try:
    n= int(input("Enter a number :"))
except:
    print("Enter integer only")
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end="")
    print()
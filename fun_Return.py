def add1():
    try:
        a = int(input())
        b = int(input())
    except ValueError:
        print("Enter only Integers")
    return a+b
sum = add1()
print(sum)
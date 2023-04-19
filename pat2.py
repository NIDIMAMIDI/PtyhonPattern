n = int(input("Enter a Number : "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()
"""
        OUTPUT

Enter a Number : 5
1
12
123
1234
12345
"""
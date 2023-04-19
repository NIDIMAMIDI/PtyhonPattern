num = int(input("Enter a number  : "))
a = 0
b = 1
c = a+b
if num <= 1:
    print("Enter a valid number")
elif num == 2:
    print(a, b)
else:
    print(a,b,  end=" ")
    for i in range(3, num+1):
        print(c,  end=" ")
        a = b
        b = c
        c = a + b 
"""
        OUTPUT
Enter a number  : 7
0 1 1 2 3 5 8

Enter a number  : 2
0 1

Enter a number  : 1
Enter a valid number
"""
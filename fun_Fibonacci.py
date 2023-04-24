def fib(n):
    if n==1:
        print(0)
    elif n == 2:
        print(0, 1)
    elif n > 2:
        a = 0
        b = 1
        print(a, b, end=" ")
        c = a + b
        count = 2
        while(count < n):
            print(c, end=" ")
            a = b
            b = c
            c = a + b
            count += 1
    else:
        print("Enter numbers that are greater than or equal to 1")
 
try:
    n = int(input())
except ValueError as err:
    print(err)
fib(n)
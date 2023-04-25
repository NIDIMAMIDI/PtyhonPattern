def find_nth_fibnoccai(n):
    if n == 1 :
        return 0
    elif n ==2:
        return 1
    elif n > 2:
        a = 0
        b = 1
        s = 1
        for i in range(3, n+1):
            c = a + b
            a = b
            b = c
            s = s + c
        return s
    else :
        return -1
try:
    n = int(input("Enter a nth term to find the number : "))
except ValueError as err:
    print("Enter Only Integers")
print(find_nth_fibnoccai(n))
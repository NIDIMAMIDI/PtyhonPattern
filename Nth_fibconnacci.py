def find_nth_fibnoccai(n):
    if n == 1 :
        return 0
    if n ==2:
        return 1
    if n <= 0:
        return -1
    return find_nth_fibnoccai(n-1)+find_nth_fibnoccai(n-2)
try:
    n = int(input("Enter a nth term to find the number : "))
except ValueError as err:
    print("Enter Only Integers")
print(find_nth_fibnoccai(n))

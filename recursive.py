def do(n):
    if n<=5:
        return
    do(n-1)
    print(n, end=" ")
    do(n-1)
    print(n, end=" ")
do(8)
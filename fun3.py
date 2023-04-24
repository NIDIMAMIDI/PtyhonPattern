def add():
    try:
        a = int(input())
        b = int(input())
    except ValueError as Err:
        print(Err)
    print(a+b)
add()
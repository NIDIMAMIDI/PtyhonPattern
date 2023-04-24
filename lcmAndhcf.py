def lcm(num1, num2):
    if num1 > num2:
        great = num1
    else:
        great = num2
    while(True):
        if great % num1 == 0 and great % num2 == 0:
            l = great
            break
        great += 1 
    print(l)
def hcf(num1, num2):
    if num1 > num2:
        n = num1
    else:
        n = num2
    while(True):
        if  num1 % n == 0 and num2 % n == 0:
            h = n
            break
        n -= 1
    print(h)
try:
    num1 = int(input())
    num2 = int(input())
except ValueError as err:
    print("Enter Integer only")
lcm(num1, num2)
hcf(num1, num2)

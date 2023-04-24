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
    if num1 <= num2:
        n = num1
    else:
        n = num2
    for i in range(1, n+1):
        if num1 % i == 0 and num2 % i == 0:
            h = i
    print(h)
try:
    num1 = int(input())
    num2 = int(input())
except ValueError as err:
    print("Enter Integer only")
lcm(num1, num2)
hcf(num1, num2)

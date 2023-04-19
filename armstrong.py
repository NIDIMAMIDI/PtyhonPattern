n = input("Enter a number  : ")
l = len(n)
num = int(n)
temp = num
arm = 0
while num > 0:
    rem = num % 10
    arm = arm  + pow(rem, l)
    num = num // 10
if temp == arm :
    print(temp, "is a armstrong number")
else:
    print(temp, "is a not armstrong number")


""""
        OUTPUT
Enter a number  : 153
153 is a armstrong number


Enter a number  : 123
123 is a not armstrong number
"""
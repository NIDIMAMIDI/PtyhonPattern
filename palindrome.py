num = int(input("Enter a number : "))
temp = num
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
if rev == temp:
    print(temp, "is a Palindrome")
else:
    print(temp, "is not a Palindrome")


"""
        OUTPUT
Enter a number : 67
67 is not a Palindrome

Enter a number : 787
787 is a Palindrome
"""
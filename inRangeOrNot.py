try:
    num = int(input("Enter a number : "))
except:
    print("Enter only integers")
for i in range(1,101):
    if i == num:
        print(num, "is between 1 and 100")
        break
else:
    print(num, "is not in between 1 and 100")

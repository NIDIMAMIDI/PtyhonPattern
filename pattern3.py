n = int(input("Enter number of rows : "))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end ="")
    print()

"""
        OUTPUT
Enter number of rows : 3
  *
 ***
*****
"""
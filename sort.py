n1 = int(input("Enter first num : "))
n2 = int(input("Enter second num : "))
n3 = int(input("Enter third num : "))
l = [n1, n2, n3]
for i in range(3):
    for j in range(3-i-1):
        if l[j] > l[j+1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp
print("Ascending order is :")
for i in l:
    print(i, end=" ")

"""
        OUTPUT
Enter first num : 34
Enter second num : 09
Enter third num : 345
Ascending order is :
9 34 345


Enter first num : 5
Enter second num : 34
Enter third num : 1
Ascending order is :
1 5 34 

"""

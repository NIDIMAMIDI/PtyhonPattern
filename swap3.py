n1=int(input("Enter number:"))
n2=int(input("Enter number:"))
n3=int(input("Enter number:"))
if(n1>n2 and n1>n3):
    if(n2<n3):
        temp=n1
        n1=n2
        n2=n3
        n3=temp
    else:
      temp=n1
      n1=n3
      n3=temp
elif n2>n1 and n2>n3:
    if(n1<n3):
      temp=n2
      n1=n3
      n3=temp
    else:
      temp=n2
      n2=n1
      n1=n3
      n3=temp
else:
      if(n1>n2):
        temp=n2
        n2=n1
        n1=temp
print(n1,n2,n3)

"""
        OUTPUT

Enter number:23
Enter number:432
Enter number:5
5 23 432
"""
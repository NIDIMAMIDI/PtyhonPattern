option = int(input("1.Traingle Area || 2. Square Area || 3. Rectangle Area : "))
if option == 1:
    base = int(input("Enter base "))
    height = int(input("Enter heifht "))
    print("Area of Traingle : ", 0.5 *(base * height))
elif option == 2:
    side = int(input("Enter side "))
    print("Area of Square : ", side * side)
elif option == 3:
    length = int(input("Enter length "))
    breadth = int(input("Enter breadth "))
    print("Area of Square : ", length * breadth)
else :
    print("Enter valid Number to find areas")

"""
        OUTPUT
1.Traingle Area || 2. Square Area || 3. Rectangle Area : 2
Enter side 5
Area of Square :  25
1.Traingle Area || 2. Square Area || 3. Rectangle Area : 1
Enter base 3
Enter heifht 2
Area of Traingle :  3.0
"""

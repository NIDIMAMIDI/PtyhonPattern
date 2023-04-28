"""Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
Explanation 0

There are  students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line."""

# code for program is ....... 

l = []
for _ in range(int(input())):
    l1= []
    name = input()
    score = float(input())
    l1.append(name)
    l1.append(score)
    l.append(l1)
    
ln = len(l)
for i in range(0, ln):
    for j in range(0, ln-i-1):
        if (l[j][1] > l[j + 1][1]):
            tempo = l[j]
            l[j]= l[j + 1]
            l[j + 1]= tempo
l2 = []

for i in range(1, ln):
    if l[i][1] == l[0][1]:
        continue
    else:
        l2.append(l[i])
        ind = i+1
        for j in range(ind, ln):
            if l2[0][1] != l[j][1]:
                break
            else:
                l2.append(l[j])
        break

l2.sort()        
for i in range(len(l2)):
    print(l2[i][0])




"""
        Output

3
sharuk
15
anu
15
xcgdf
2
anu
sharuk



5
harsh
20
beria
20
varun
10
kakumai
10
vikas
21
beria
harsh

"""
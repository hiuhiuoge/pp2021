print("----Student List----")

D = dict()
s = int(input('number of students:'))

for i in range(0,s):
    x, y = input("Enter the complete name (First and last name) of student: ").split()
    n = input('student DOB: ')
    i = input('student ID: ')
    k = input('name of the course: ')
    p = input('point: ')
    D[x, y] = (z, m, n, i, k, p)


print(D)
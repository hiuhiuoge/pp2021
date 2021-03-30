print("----Student List----")

D = dict()
s = int(input('number of students:'))

for i in range(0,s):
    x, y = input("Enter the complete name (First and last name) of student: ").split()
    n = input('student DOB: ')
    i = str(input('student ID: '))
    k = [str(input('name of the course: ')), str(input('point: '))]
    D[x, y] = (n, i, k)


print(D)

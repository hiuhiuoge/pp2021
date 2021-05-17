print("----Student List----")

D = dict()
s = int(input('number of students:'))

for i in range(0,s):
    x, y = input("Enter the complete name (First and last name) of student: ").split()
    n = input('student DOB: ')
    i = str(input('student ID: '))
    k = str(input('name of the course: '))
    l = str(input('point: '))
    D[x, y] = (n, i, k, l)

class Student:
    def Student(self):
        self._name = x, y
        self._DoB = n
        self._ID = i

    def getStudent(self):
        return self._name
        return self._DoB
        return self._ID

class Course:
    def Course(self):
        self._course = k
        self._mark = l

    def getCourse(self):
        return self._course
        return self._mark
        
print(D)

class Course:
    ls = []

    def __init__(self):
        self.__name = ''
        self.__id = ''
        self.__score = 'N/A'

    def getId(self):
        return self.__id

    def setScore(self, sc):
        self.__score = sc

    def input(self):
        self.__name = input('Name: ')
        self.__id = input('Id: ')

    def display(self):
        print('Name: ', self.__name)
        print('Id: ', self.__id)
        print('Score: ', self.__score)

    def list(self):
        for i in self.ls:
            i.display()


class Student:
    ls = []

    def __init__(self):
        self.__name = ''
        self.__dob = ''
        self.__id = ''

    def input(self):
        self.__name = input('Name: ')
        self.__id = input('Id: ')
        self.__dob = input('DOB: ')
        b = int(input('Number of courses: '))
        for j in range(b):
            a = Course()
            a.input()
            Course().ls.append(a)

    def setScore(self):
        s = str(input("Enter course id or 'exit' if you are done: "))
        while s != 'exit':
            flag = True
            for k in Course().ls:
                if k.getId() == s:
                    k.setScore(input('Score: '))
                    flag = False
                    break
            if flag:
                print('Course Id not found!')
            s = str(input("Enter course id or 'exit' if you are done: "))

    def findScore(self):
        s = str(input("Enter course id or 'exit' if you are done: "))
        while s != 'exit':
            flag = True
            for k in Course().ls:
                if k.getId() == s:
                    self.display()
                    k.display()
                    flag = False
                    break
            if flag:
                print('Course Id not found!')
            s = str(input("Enter course id or 'exit' if you are done: "))

    def display(self):
        print('Name: ', self.__name)
        print('Id: ', self.__id)
        print('DOB: ', self.__dob)
        for i in self.__ls:
            i.display()

    def list(self, lst):
        for j in lst:
            j.display()


if __name__ == "__main__":
    a = int(input('Number of students: '))
    students = []
    for _ in range(a):
        student = Student()
        student.input()
        student.setScore()
        students.append(student)
    Student().list(students)
print("----Student List----")
import math
import numpy as np
from random import randint, seed

class input:
    D = dict()
    s = int(input('number of students:'))
    class Student:
        def __init__(self, x, y, n, i):
            self.name = (x, y)
            self.DoB = n
            self.ID = i


    class Course:
        def __init__(self, k):
            self.course = k
        

    for i in range(s):
        x, y = input("Enter the complete name (First and last name) of student: ").split()
        n = input('student DOB: ')
        i = str(input('student ID: '))
        ci = int(input('number of courses:'))
        s = Student(x, y, n, i)
        c = Course({})
        for j in range(ci):
            k = str(input('name of the course: '))
            l = math.floor(float(input('point: ')) * 10)/10
            c.course[k] = l
        D[s] = c
    seed(1)

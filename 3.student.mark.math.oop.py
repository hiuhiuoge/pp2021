print("----Student List----")
import math
import numpy as np
from random import randint, seed

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
def cal_gpa(name):
    for key in D:
        if name in str(key.name[0]) + ' ' + str(key.name[1]):
            sco = np.array([D[key].course[ke] for ke in D[key].course])
            cre = np.array([randint(1,5) for i in range(len(sco))])
            return tuple((name, math.floor(sco.dot(cre)/sum(cre)*10)/10))
def sort():
    ls = []
    for key in D:
        ls.append(cal_gpa(str(key.name[0]) + ' ' + str(key.name[1])))
    for i in sorted(ls, key = lambda x : x[1], reverse=True):
        print(i[0] + ': ' + str(i[1]))
<<<<<<< HEAD
sort()
=======
sort()
>>>>>>> 3842d98f325dd1655f2883bbca233f10a91e7ab4

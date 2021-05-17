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

    def compress(self, nameFile):
            list_files = ['students.txt','courses.txt']
            
            compression = zipfile.ZIP_DEFLATED
            z = zipfile.ZipFile(nameFile, mode="w")
            
            for file in list_files:
                z.write(file, file, compress_type=compression)
            z.close()
            
    def decompress(self):
        try: 
            with zipfile.ZipFile("students","r") as zip_ref:
                zip_ref.extractall("decompress")
        except Exeption as e:
            print('students not found')
            print('error :',e)
        
    def writeFile(self, st):
        for i in st:
            with open("students.txt", "a+") as f1:
                f1.write("Name: "+i.Name+'\n')
                f1.write('Id: '+i.Id+'\n')
                f1.write('DOB '+i.DOB+'\n')

            with open('courses.txt','a+') as f2:
                f2.write('Name :'+i.Name+'\n')
                for j in i.courses:
                    f2.write('Name of the course:'+j[0]+'\n')

            with open('marks.txt','a+') as f3:
                f3.write('Name :'+i.stName+'\n')
                for j in i.courses:
                    f3.write(f'{j[0]}:'+j[1]+'\n')
    f1.close()
    f2.close()
    f3.close()
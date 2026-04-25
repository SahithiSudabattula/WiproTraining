#driver_code

from OOP_concepts.college import College
from OOP_concepts.student import Student
from OOP_concepts.studentgrade import StudentGrade
from OOP_concepts.teacher import Teacher

cc = int(input('C Code: '))
cn = input('C Name: ')
ci = input('C City: ')
rno = int(input('Roll no: '))
sn = input('Student name: ')
m1 = int(input('M1: '))
m2 = int(input('M2: '))
m3 = int(input('M3: '))
eid = int(input('Employee id: '))
tn = input("Ten Name: ")
de = input('Dept Name:')
bp = float(input('Bp: '))



# project = College(ccode=cc, cname=cn, ccity=ci)
#
# project.welcome_message()
# project.display_college_details()

# project = Student(ccode=cc, cname=cn, ccity=ci, rno = rno, sname= sn,
#                   m1=m1, m2=m2, m3=m3)

project = StudentGrade(ccode=cc, cname=cn, ccity=ci, rno = rno, sname= sn, m1=m1, m2=m2, m3=m3)


project.welcome_message()
project.display_college_details()
print(f'Roll No: {project.rollno} \t Name: {project.stuname} \nTotal: {project.calculate_total()} \nAverage: {project.calculate_average()}')
project.calculate_grade()

print(f'Result: {project.result} \t Grade: {project.grade}')

teach = Teacher(ccode = cc, cname=cn, ccity=ci, eid=eid, tn=tn, de=de, bp=bp)
print(f'Eid: {teach.empid} \t Name: {teach.tname} \t Dept: {teach.dept}')
print(f'Salary: {teach.calculate_salary()}')
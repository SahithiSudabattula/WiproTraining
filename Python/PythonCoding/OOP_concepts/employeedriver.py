from OOP_concepts.employeedetails import EmployeeDetails

#driver
eno = int(input('Emp no : '))
name = input('Emp name: ')
bp = float(input('basic pay: '))

employee = EmployeeDetails(empno = eno, ename=name, basicpay=bp)
# print('Emp no: ', employee.get_empno())

print('Emp no: ',employee.empno)
print('Emp name: ', employee.ename)
print('Basic Pay: ', employee.basic_pay)
print('Salary: ',employee.calculate_netsal())

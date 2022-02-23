
employees = ['Hasan', 'Hadi', 'Reem', 'Ahmad']

print(employees)
print(employees[0])
print(employees[2])
print(employees[3])
print(employees[-1])
print(employees[-3])
print(employees[50])

print(employees[1:3])
print(employees[:3])
print(employees[1:])
print(employees[0:4:1])
print(employees[::1])
print(employees[::2])

print(employees)
employees[1] = 'sara'
print(employees)

employees[-1] = 'yara'
print(employees)

employees[0:2] = 'Hadi', 'Salwa'
print(employees)

employees[0:2] = ''
print(employees)

print('------------------------------------------------')
# for loop
employees = ['Hasan', 'Hadi', 'Reem', 'Ahmad']

for i in range(4):
    print(employees[i])

for i in range(4):
    print(i)

for i in range(len(employees)):
    print(employees[i])

for i in range(len(employees)):
    print(f'index {i} in employees is: {employees[i]}')

print('------------------------------------------------')

# enumerate
for index,item in enumerate(employees):
    print(f'index {index} in employees is: {item}')

print('------------------------------------------------')

# in and not in
print('Hadi' in employees)
print('Hadi' not in employees)


# print('أدخل اسم الموظف:')
# name = input()
# if name not in employees:
#     print('ليس لدينا موظف اسمه ' + name)
# else:
#     print(f' هو موظف في الشركة {name}')


print('------------------------------------------------')
# random.choice() and random.shuffle()
import random
employees = ['Hasan', 'Hadi', 'Reem', 'Ahmad']
print(random.choice(employees))
print(random.choice(employees))
print(random.choice(employees))
random.shuffle(employees)
print(employees)
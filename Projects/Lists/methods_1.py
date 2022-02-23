# append and insert
employees = ['Hasan', 'Hadi', 'Reem', 'Ahmad']
employees.append('yara')
print(employees)

employees.insert(1, 'sara')
print(employees)

oldEmployees = ['osama', 'Alaa']
employees.append(oldEmployees)
print(employees)
print(employees[6])
print(employees[6][0])

print('------------------------------------------------')
# extend
employees = ['Hasan', 'Hadi', 'Reem', 'Ahmad']
oldEmployees = ['osama', 'Alaa']

employees.extend(oldEmployees)
print(employees)

print('------------------------------------------------')
# remove
employees.remove('Reem')
print(employees)

# employees.remove('anas')

employees = ['Hasan', 'Hadi', 'Hasan', 'Ahmad']
employees.remove('Hasan')
print(employees)

print('------------------------------------------------')
# del statement
del employees[0]
print(employees)

print('------------------------------------------------')
#sort
numbers = [2, 5, 3.14, 1, -7]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

employees = ['Yara', 'Sara', 'Hasan', 'Ahmad']
employees.sort()
print(employees)

employees.sort(reverse=True)
print(employees)

# spam = [1, 3, 2, 4, 'Alice', 'Bob']
# spam.sort()

print('------------------------------------------------')
# reverse
employees = ['Yara', 'Sara', 'Hasan', 'Ahmad']
employees.reverse()
print(employees)
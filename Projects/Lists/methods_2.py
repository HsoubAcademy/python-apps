# index
employees = ['Hasan', 'Hadi', 'Reem', 'Ahmad', 'Hadi']
print(employees.index('Hadi'))
# print(employees.index('sara'))

print('------------------------------------------------')
# count
print(employees.count('Hadi'))
print(employees.count('Reem'))

print('------------------------------------------------')
# copy
test = employees.copy()
print(employees)
print(test)

print('------------------------------------------------')
# clear
employees.clear()
print(employees)
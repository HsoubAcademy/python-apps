# get

hadi = {
    'name' : 'hadi',
    'number' : '7645214781',
    'skills' : ['HTML', 'CSS', 'Bootstrap']
}

# print(hadi['name'] + ' receives a salary of ' + str(hadi['salary']))

print(hadi['name'] + ' receives a salary of ' + str(hadi.get('salary', 'no salary')))

print('---------------------------------------')
# setdefault
print(hadi)
print(hadi.setdefault('name' , 'sara'))
print(hadi)
print(hadi.setdefault('salary' , 2000))
print(hadi)

if 'language' not in hadi:
    hadi['language'] = 'CSS'
print(hadi)

print('---------------------------------------')
# update
numbers = {1: "one", 2: "three"}
print(numbers)
numbers.update({2:"Two"})
print(numbers)
numbers.update({3:"Three"})
print(numbers)


print('---------------------------------------')
# clear
print(hadi)
hadi.clear()
print(hadi)
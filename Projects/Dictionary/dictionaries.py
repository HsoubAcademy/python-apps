# names = ['Hadi', 'Yara', 'Hasan', 'Sara', 'Osama']
#
# salary = [1000, 500, 2000, 600, 800]
#
# numbers = ['7645214781', '654789526', '4478965662', '998745625', '5547896456']

# Dictionaries
hadi = {
    'name' : 'hadi',
    'salary' : 2000,
    'number' : '7645214781',
    'skills' : ['HTML', 'CSS', 'Bootstrap']
}

print(hadi)
print(hadi['skills'])
print(hadi['number'])

print('----------------------------------')
list = ['cats', 'dogs', 'moose']
myList = ['dogs', 'moose', 'cats']
print(list==myList)
print(list[0])
print(myList[0])

print('----------------------------------')
dictionary = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
myDictionary = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(dictionary==myDictionary)
print(dictionary['age'])
print(myDictionary['age'])


# print('----------------------------------')
# birthdays = {'hadi': 'Apr 1', 'sara': 'Dec 12', 'yara': 'Mar 4'}
# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break
#
#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')


print('----------------------------------')
hadi = {
    'name' : 'hadi',
    'salary' : 2000,
    'number' : '7645214781',
    'skills' : ['HTML', 'CSS', 'Bootstrap']
}
print(hadi.keys())
print(hadi.values())
print(hadi.items())

print('----------------------------------')
# get
yara = {
    'frontEnd' : {
        1: 'HTML',
        2: 'CSS',
        3: 'Bootstrap'
    },
    'backEnd': {
        1: 'PHP',
        2: 'Node.js'
    }
}
print(yara)
print(yara['frontEnd'])
print(yara['backEnd'])
print(yara['frontEnd'][2])
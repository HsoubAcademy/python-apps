name = 'Hadi'
age = 29

# print('Hello, my name is ' + name + '. I am ' + age  + ' years old.')
print('Hello, my name is ' + name + '. I am ' + str(age)  + ' years old.')
print('My name is %s. I am %d years old.' % (name, age))

rank = 9.0
print('My name is %s. I am %d years old. my rank is %.2f' % (name, age, rank))

print('----------------------------- % ----------------------------------')
first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"
print("Hello, %s %s. You are %s. You are a %s. You were a member of %s." % (first_name, last_name, age, profession, affiliation))

print('----------------------- str.format -------------------------------')

print('My name is {}. I am {} years old.'.format(name, age))
print('My name is {:s}. I am {:d} years old. my rank is {:.3f}'.format(name, age, rank))
print('My name is {1}. I am {0} years old.'.format(age, name))
print('My name is {name_key}. I am {age_key} years old.'.format(name_key = name, age_key = age))

first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"
print(("Hello, {first_name} {last_name}. You are {age}. " +
        "You are a {profession}. You were a member of {affiliation}.") \
        .format(first_name=first_name, last_name=last_name, age=age, \
                profession=profession, affiliation=affiliation))

print('----------------------- f-string -------------------------------')
print(f'My name is {name}. I am {age} years old.')
print(f'My name is {name}. my age next year is {age+1}')
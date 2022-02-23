# join
list = ['Hello', 'world']
print(' '.join(list))
print('-'.join(list))
print('ABC'.join(list))
print(type('ABC'.join(list)))

print('------------------------------------------------------')
# split
test = 'Hello world'
print(test.split(' '))

test = 'MyABCnameABCisABCHadi'
print(test.split('ABC'))

test = '''Hello
how are you?
thanks, i am fine'''
print(test.split('\n'))

print('------------------------------------------------------')
# splitlines
test = '''Hello
how are you?
thanks, i am fine'''
print(test.splitlines())

test = 'Hello\nhow are you?\nthanks, i am fine'
print(test)
print(test.splitlines())
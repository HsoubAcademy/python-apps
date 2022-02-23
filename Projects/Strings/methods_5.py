# index(substring, start, end)
test = 'Hello world'
print(test.index('world'))
print(test.index('o'))
# print(test.index('world', 0, 5))
try:
    print(test.index('world', 0, 5))
except ValueError:
    print('-1')

print('------------------------------------------------------')
# find(substring, start, end)
test = 'Hello world'
print(test.find('world'))
print(test.find('world', 0, 5))

print('------------------------------------------------------')
# replace(old value, New value, Count)
text ="one plus one equal two"
print(text.replace("one", "1"))
print(text.replace("one", "1", 1))
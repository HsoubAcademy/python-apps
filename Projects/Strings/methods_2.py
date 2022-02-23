# startswith, endswith
test = 'Hello, world'
print(test.startswith('Hello'))
print(test.startswith('world'))
print(test.endswith('world'))

print(test.startswith('H'))
print(test.endswith('d'))
print(test.startswith('w', 7, 11))

print('------------------------------------------------------')
# strip, rstrip, lstrip
test = '    Hello, world    '
print(test)
print(test.strip())
print(test.lstrip())
print(test.rstrip())

test = '@@@Hello, world@@@'
print(test)
print(test.strip('@'))
print(test.lstrip('@'))
print(test.rstrip('@'))

test = '@#@#@#Hello, world@#@#@#'
print(test)
print(test.strip('@#'))
print(test.lstrip('@#'))
print(test.rstrip('@#'))

print('------------------------------------------------------')
# zfill
hours = "1"
min = "9"
sec = "5"

print(f'{hours}:{min}:{sec}')
print(f'{hours.zfill(2)}:{min.zfill(2)}:{sec.zfill(2)}')
print(f'{hours.zfill(3)}:{min.zfill(3)}:{sec.zfill(3)}')

hours = "1"
min = "19"
sec = "25"
print(f'{hours.zfill(2)}:{min.zfill(2)}:{sec.zfill(2)}')
print(f'{hours.zfill(3)}:{min.zfill(3)}:{sec.zfill(3)}')
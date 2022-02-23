import re
def isPhoneNumber(text):
    is_phone = re.search(r'\d{3}-\d{3}-\d{4}', text)

    if is_phone:
        print(f'the {text} is a valid phone number')

    else:
        print(f'the {text} is not a valid phone number')

print('Is 415-555-4242 a phone number?')
isPhoneNumber('415-555-4242')
print('Is Hello hello a phone number?')
isPhoneNumber('Hello hello')
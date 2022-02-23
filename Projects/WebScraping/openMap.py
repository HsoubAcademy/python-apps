import webbrowser, sys

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])

else:
    print('Please enter the address')

webbrowser.open('https://www.google.com/maps/place/' + address)
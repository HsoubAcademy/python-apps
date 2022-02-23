import imapclient

# connect to server
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

# login to email
rec_email = "academyhsoub1@gmail.com"
password = input(str("Please enter your password: "))
imapObj.login(rec_email, password)

# print all folders
import pprint
pprint.pprint(imapObj.list_folders())

# select folder
imapObj.select_folder('INBOX', readonly=True)

# Search in folder
UIDs = imapObj.search(['ALL'])
print(UIDs)

rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
#pprint.pprint(rawMessages)

import pyzmail

message = pyzmail.PyzMessage.factory(rawMessages[73][b'BODY[]'])
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))


# get message body
print(message.text_part.get_payload().decode(message.text_part.charset))
print(message.html_part.get_payload().decode(message.text_part.charset))

imapObj.logout()
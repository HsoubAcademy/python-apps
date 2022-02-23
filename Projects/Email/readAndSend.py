import ezgmail

print(ezgmail.EMAIL_ADDRESS)

#ezgmail.send('academyhsoub1@gmail.com', 'Test line', 'Test Body of the email', ['test.jpg', 'test1.jpg'])

# get the unread messages
# unreadmessages = ezgmail.unread()
# print(ezgmail.summary(unreadmessages))
# print(len(unreadmessages))
# print(unreadmessages[0].messages[0])
# print(unreadmessages[0].messages[0].subject)
# print(unreadmessages[0].messages[0].body)
# print(unreadmessages[0].messages[0].timestamp)
# print(unreadmessages[0].messages[0].sender)
# print(unreadmessages[0].messages[0].recipient)

# get the recent messages
recentThreads = ezgmail.recent()
print(len(recentThreads))

recentThreads = ezgmail.recent(maxResults=50)
print(len(recentThreads))

# Search
resultThreads = ezgmail.search('amazon')
print(len(resultThreads))


import smtplib

sender_email = "academyhsoub1@gmail.com"
rec_email = "academyhsoub1@gmail.com"
password = input(str("Please enter your password: "))
message = "Subject: Python message.\nHello, This message sent using Python"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login successs")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)
server.quit()
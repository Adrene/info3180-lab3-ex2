import smtplib

fromaddr = 'adrene.mcintosh@gmail.com'

toaddr  = ['adrene.mcintosh6@gmail.com']

#message = """From: {} <{adrene.mcintosh@gmail.com}>

#To: {To Person} <{adrene.com}>

#Subject: {SMTP e-mail test}

#{}"""
message = """Honesty and consistency"""
Subject = "What's the wave?"
messagetosend = message.format(
                             fromaddr,


                             toaddr,


                             message)

# Credentials (if needed)

username = ''

password = ''


# Prepare actual message

message = """\
fromaddr: %s
toaddr: %s
messagetosend: %s
%s
""" % (fromaddr, ", ".join(toaddr), messagetosend, Subject)

# Send the mail

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddr, messagetosend)

server.quit()

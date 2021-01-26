import smtplib 
#Importing the smtplibb  library 
server = smtplib.SMTP('smtp.gmail.com', 587)
#tellingthe server trust transport security
server.starttls()
#Telling the server who we are
server.login('Jdog1500xx@gmail.com', 'Josh1995@10')
#Sending the email, there is going to be three parameters int his email 1: the person sending the email, 2: who you are sending it to, 3: the nessage.
server.sendmail('Jdog1500xx@gmail.com', 
                'joshuaalabre@gmail.com',
                'Hey wanna play some poker tomorrow evening?'

)


import smtplib
#Importing the smtplibb  library 
server = smtplib.SMP('smtp.gmail.com', 587)
#tellingthe server trust transport security
server.strarttls()
#Telling the server who we are
server.login('fresh.grandpa21@gmail.com', 'theoldies1954')
#Sending the email, there is going to be three parameters int his email 1: the person sending the email, 2: who you are sending it to, 3: the nessage.
server.sendmail('fresh.grandpa21@gmail.com', 
                'finestmanalive21@gmnail.com',
                'Hey wanna play some poker tomorrow evening?'

)


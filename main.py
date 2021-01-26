import smtplib 
#Importing the smtplibb  library 
import speech_recognition as sr
#Import speech Recognition using PyAudio 
listener = sr.Recognizer()
#Create a listening body hiding in the python code

#The micriphone will be a source,where the python code is going to listen for your voice on the microphone.
#And the information in the audio will return as a text and print that out using the goolge Api
try:
    with sr.Microphone() as source:
        print('listening....')
        voice = listener.listen(source)
        info = listener.recognize_google(voice)
        print(info)
except:
        pass
def send_email():
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


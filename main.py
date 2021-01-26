import smtplib 
#Importing the smtplibb  library 
import speech_recognition as sr
#Import speech Recognition using PyAudio 
#Import python text to speech
import pyttsx3
from email.message import EmailMessage
listener = sr.Recognizer()
engine = pyttsx3.init()
#Create a function called talk and its going to have the parameter text and it eill wait for the text and await foir it.
def talk(text):
    engine.say(text)
    engine.runAndWait()




#The micriphone will be a source,where the python code is going to listen for your voice on the microphone.
#And the information in the audio will return as a text and print that out using the goolge Api
def get_Info():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
            pass
        #Put the send email into a function . 
def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #tellingthe server trust transport security
    server.starttls()
    #Telling the server who we are
    server.login('Jdog1500xx@gmail.com', 'Josh1995@10')
    email = EmailMessage()
    email['From'] = 'jdog1500xx@gmail.com'
    email ['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    #Sending the email, there is going to be three parameters int his email 1: the person sending the email, 2: who you are sending it to, 3: the nessage.
    server.sendmail(email)



email_list = {
    


}

def get_email_info():
    talk('To whom you want to send the email to')
    name = get_Info()
    reciever = email_list[name]
    print(reciever)
    talk('What is the subject of the email?')
    subject = get_info()
    print(subject)
    talk('Tell me the text in your email')
    message = get_info()
    print(message)

    send_email(reciever,subject,message )


get_email_info()
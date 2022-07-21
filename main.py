from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from http import server
from ipaddress import ip_address
from msilib.schema import MIME
import time
from numpy import count_nonzero
import pyaudio
import pyttsx3
import speech_recognition as sr
from logging import exception
import datetime
import os
import cv2
import random
from requests import get
import requests
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pyautogui
import instaloader
import instadownloader



#voice engine

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
#print (voices[0].id)


def speak(audio): 
    engine.say(audio)
    print (audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source, timeout=2, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}")

    except Exception as e:
        speak("Say that again please...")  
        return "none"  
    return query  

def wish():
    hour = (datetime.datetime.now().hour)
    now = datetime.datetime.now()
    tt = now.strftime("%I:%M %p")

    if hour>=0 and hour<=12:
        speak(f"Good morning, its {tt}")

    elif hour>12 and hour<18:
        speak(f"Good Afternoon, its {tt}")
    
    else:
        speak(f"Good Evening, its {tt}")

    speak("i am era, a helping bot, how may i help you")


def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('testmail527527@gmail.com', 'hgeqnduoywhbvgkn')
    server.sendmail('testmail527527@gmail.com', to, content)

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=bdb59b9ef1094b699bbf826ff8eca415'

    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day=["first","second","third","forth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")


if __name__ == "__main__":
    wish()
    while True:
    
        

        query = takecommand().lower()




#opening application

        if "open notepad" in query:
            speak('opening notepad')
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
            os.startfile(npath)

        elif "open chrome" in query:
            speak('opening Google chrome')
            cpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
            os.startfile(cpath)

        elif "open excel" in query:
            speak('opening microsoft excel')
            epath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\Microsoft Office\\Microsoft Office Excel 2007.lnk"
            os.startfile(epath)

        elif "open word" in query:
            speak('opening miicrosoft word')
            wpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk"
            os.startfile(wpath)

        elif 'open python' in query:
            speak('opening python IDELE')
            ppath = "C:\\Users\HP\\AppData\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.10\\IDLE (Python 3.10 64-bit).lnk"
            os.startfile(ppath)

        elif 'open my files' in query:
            speak("opening your files")
            os.system("start explorer")             

        elif "open command prompt" in query:
            speak("opening command prompt")
            os.system("start cmd")


        
        elif 'open camera' in query:
            speak('opening Webcam')
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(58)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

#closing application

        elif 'close notepad' in query:
            speak("closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'close chrome' in query:
            speak('closing chrome')
            os.system('taskkill /f /im chrome.exe')


        elif 'close python' in query:
            speak('closing python IDELE')
            os.system('taskkill /f /im pythonw.exe')

        elif 'close excel' in query:
            speak('closing microsoft excel')
            os.system('taskkill /f /im excel.exe')

        elif 'close word' in query:
            speak ('closing microsoft word')
            os.system('taskkill /f /im winWord.exe')


#Greetings
        elif 'what is your name' in query:
            speak('I am ERA')

        elif "what's your name" in query:
            speak('I am ERA')            
        
        elif 'who are you' in query:
            speak('I am ERA, bot designed by ,chandramauli ,to do all your basic tasks')

        elif 'how are you' in query:
            speak('i am fine, always good to go, what about you')    

        elif 'i am fine' in query:
            speak('ooh Thats great, happy to hear that')
            
        elif 'i am fine too' in query:
            speak('ooh Thats great, happy to hear that')

        elif 'not fine' in query:
            speak('ooh... sorry to hear that, shall i tell you a joke to make you happy')
            jk = takecommand().lower()
            if jk == 'yes':
                joke = pyjokes.get_joke()
                speak(joke)

            else:
                speak('as your wish, hope you will get better soon')

        elif 'thanks' in query:
            speak('always happy to hear that, thanks for praising me')


        #elif "my father's" in query or "fathers name" in query:
            #speak("Your father's name is Ravi Shankar Ravi")
            

#to tell joke

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            speak('shall i tell another one')
            jk2 = takecommand().lower()
            if jk2 == 'yes':
                joke = pyjokes.get_joke()
                speak(joke)

            else:
                speak("As your wish...") 
                



#to crash window
        elif 'crash this window' in query:
            speak('are you sure, you want to crash this window')
            cr = input("yes or no => ")
            if cr == 'yes':
                speak('Enter the security code for crashing this window')
                cr2 = input("==> ")
                if cr2 == "Ggglvxy":
                    speak("Crashing this window in 5")
                    speak("4")
                    speak("3")
                    speak("2")
                    speak("1")
                    speak("Window is successfully Crashed")
                    os.system('taskkill /f /im explorer.exe')
                else:
                    speak('Wrong password... terminating window')
                    sys.exit()

            elif cr == 'no':
                speak("As your wish window carsh unsuccessfull")

            else:
                speak("INVALID INPUT")





#find ip address

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

#search on wikipedia

        elif "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            speak(results)
            print(results)

#opening web pages

        elif "open youtube" in query:
            speak('opening youtube on google')
            webbrowser.open("youtube.com")

        elif "open stack overflow" in query:
            speak('opening stack overflow on google')
            webbrowser.open("stackoverflow.com")

        elif "open instagram" in query:
            speak("opening instagram on google")
            webbrowser.open("instagram.com")

        elif "open python webpage" in query:
            speak('opening python web page')
            webbrowser.open("python.org")

        elif "open google" in query:
            speak('what should i search sir')
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")


#to switch the window

        elif 'switch the window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp("alt")

#for news updates

        elif "news" in query:
            speak("Please wait, fetching today's letest news") 
            news()   


#set alarms

        elif 'set alarm' in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = 'D:\\python\\E.R.A bot\\alarm'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))




#send messages through whatsapp


        elif "send message" in query:
            speak("Enter the mobile number with country code")
            msg1 = input("==> ")

            speak("Enter the message")
            msg2 = input("==> ")

            speak("Enter the time in hour")
            msg3 = int(input("==> "))

            speak("Enter the time in minute")
            msg4 = int(input("==> "))

            kit.sendwhatmsg(msg1, msg2,msg3,msg4)


#To take screenshorts

        elif "take screenshot" in query or "take a screenshot" in query:
            speak("Please tell me the name of screenshot file")
            name = takecommand().lower()
            speak("please hold for a second, i'm taking screenshot")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i'm done, the screnshot is saved in our main folder")




#check instagram profile

        elif "intagram profile" in query or "profile on instagram" in query:
            speak("Enter the username correctly")
            name = input("==> ")
            webbrowser.open(f"https://instagram.com/{name}")
            speak(f"Here you go, this is the profile of {name}")
            time.sleep(5)
            speak("Would you like to download the profile picture of this account")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only = True)
                speak("I am done, profile picture is saved in our main folder")
            elif "no" in condition:
                speak("Ok, as your wish")

            else :
                speak("Invalid input")
                pass 

        elif 'play song' in query:
            speak("Enter the name of song accurately")
            ytsong = input("==> ")
            speak(f"playing {ytsong} on youtube")
            kit.playonyt(ytsong)


#to find location

        elif "where are we" in query or "find my location" in query:
            r = requests.get('https://geojs.io/')
            speak("wait, let me check")
            speak("fetching you IP address")

            ip_request =  requests.get('https://get.geojs.io/v1/ip.json')
            ipAdd = ip_request.json()['ip']
            print(ipAdd)
            speak("Got you IP address successfully")
            speak(f"you ip address is {ipAdd}")
            speak("now, checking your location")
            url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
            geo_request = requests.get(url)
            geo_data = geo_request.json()
            #print(geo_data)

            lat = (geo_data['latitude'])
            longi = (geo_data['longitude'])
            #print(geo_data['city'])
            #print(geo_data['region'])
            country = (geo_data['country'])



            speak (f"you are at GAYA state, in region of BIHAR, in {country}, you latitute is {lat} and longitude is {longi}")



#Send emails           

        elif 'send email' in query:
            
            speak('what should i send')
            query = takecommand().lower()
            if  'send a file' in query:
                email = 'testmail527527@gmail.com'
                password = 'hgeqnduoywhbvgkn'
                speak("Enter the email of reciver")
                send_to_email = input("==> ")
                speak("ok, what will be the subeject for email")
                query = takecommand().lower()
                subject = query
                speak("and what is the message for this email")
                query2 = takecommand().lower()
                message = query2
                speak('please enter the correct path of your file in shell') 
                file_location = input('==> ')

                speak('please wait, sending this email')

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)

                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak(f'Email has been successfully sent to {send_to_email}')

            elif 'send a text message' in query:
                email = 'testmail527527@gmail.com'
                password = 'hgeqnduoywhbvgkn'
                speak("Enter the email of reciver")
                send_to_email = input("==> ")
                message = query

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(email, password)
                server.sendmail(email, send_to_email, message)
                server.quit()
                speak(f"Email hast been sent to {send_to_email}")

            else:
                speak('invalid input, try saying "SEND A FILE" or "SEND A TEXT MESSSAGE"')
                



                


#to do power settings

        elif 'shut down the system' in query:
            speak("shuting down the system in 1.5 seconds")
            os.system('shutdown /s /t 5')

        elif 'restart the system' in query:
            speak("restating the system in 1.2 seconds")
            os.system('shutdown /r /t 5')

        elif 'sleep the system' in query:
            speak("making you system sleep in 0.8 seconds")
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')    


#closing ERA bot

        elif "quit" in query:
            speak("Thanks, i can quit now, have a good day")
            sys.exit()




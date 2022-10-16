import pyttsx3 as p
import speech_recognition as sr
import pywhatkit as do
import datetime
import pyjokes as j
import webbrowser as w
import wikipedia as wiki
from playsound import playsound as play
import time
import people_also_ask as answer
import AppOpener as app
avoice=1
aname="alexa"
call=''
work=''

def task(text):
    if("story" in text):
        text="Once upon a time in a fairy tale land a cat and a dog were friends. One night, the cat invited the dog for a party at his house.The cat played the fiddle. The dog happily clapped his hands. Suddenly, they saw a cow flying in the sky. It jumped over the moon. The dog laughed. Just then, they saw a dish and a spoon from the party running away together. And they laughed even louder. After that they became the best friends."
        speak("say character 1")
        print("character 1:")
        time.sleep(2)
        print("dog")
        speak("say character 2")
        print("character 2:")
        time.sleep(2)
        print("cat")
        speak("say character 3")
        print("character 3:")
        time.sleep(2)
        print("end")
        speak("story time")
        print("story time")
        speak(text)
        return

    text1=text.split()
    ans=answer.get_simple_answer(text)
    if(ans!='' and (text1[0]=="meaning" or text1[0]=='where' or text1[0]=='what' or text1[0]=='who' or text1[0]=='which' or text1[0]=='why' or text1[0]=='when' or text1[0]=='is' or text1[0]=='is')):
        print(ans)
        speak(ans)
        text=''
        return
    else:
        if(text1[0]=='where' or text1[0]=='what' or text1[0]=='who' or text1[0]=='which' or text1[0]=='why' or text1[0]=='when' or text1[0]=='is' or text1[0]=='is'):
            do.search(text)
            text=''
            return
        if('tell me something about' in text):
            text=text.replace('tell me something about','')
            try:
                text=do.info(text)
            except:
                pass
            print(text)
            speak(str(text))
            text=''
            return
        if("open" in text):
            speak("opening")
            if("classroom" in text):

                w.open("https://classroom.google.com/h")
            else:
                text=text.replace("open","")
                app.run(text)
            return
        if ('information' in text):
            index=text1.index("information")
            for i in range(index+2):
                text=text.replace(text1[i],'')
            try:
                text = do.info(text)
            except:
                pass
            print(text)
            speak(text)
            text=''
            return
        #if("change" in text and 'voice' in text):
         #   if (avoice==1):
          #      avoice==0
           # elif (avoice==0):
            #    avoice=1
        if('joke' in text or 'jokes' in text):
            text=j.get_joke()
            print(text)
            speak(text)
            text=''
            return
        if("play" in text):
            speak("playing")
            song=text.replace("play",'')
            do.playonyt(song)
            return
        if("time" in text and 'now' in text):
            text=datetime.datetime.now().strftime('%I:%M %p')
            print(text)
            speak("current time is "+text)
            return
        if('date' in text and 'today' in text):
            text = datetime.datetime.now().strftime('%dth %B %Y')
            print(text)
            speak("today's date is "+text)
            return
        if ('day' in text and 'today' in text):
            text = datetime.datetime.now().strftime('%A')
            print(text)
            speak("today's is " + text)
            return
        if ("search" in text):
            if ('for' in text):
                k="search for"
            elif ('about' in text):
                k="search about"

            else:
                k='search'
            text=text.replace(k,"")
            speak("searching")
            do.search(text)
            return
        if ('message' in text):
            print("mobile no:")
            speak("mobile number")
            mob=command()
            mob=mob.replace(" ","")
            print("message")
            speak("say your message")
            message=command()
            h=datetime.datetime.now().strftime('%I')
            #[h,m1]=timenow.split()
            h=int(h)
            m1 = datetime.datetime.now().strftime('%M')
            m1=int(m1)
            #do.sendwhatmsg('+91'+mob,message=message,time_hour=h,time_min=m1,wait_time=10,close_time=5)
            return
    call=''
    text=''
    print("try again")
    speak("try again")
    return 0


def speak(text):
    e = p.init()
    voices = e.getProperty('voices')
    e.setProperty('voice', voices[avoice].id)
    e.setProperty('rate', 150)
    e.say(text)
    e.runAndWait()
    return
def command():
    r=sr.Recognizer()
    try:
        with sr.Microphone() as m:
            r.pause_threshold=1
            r.adjust_for_ambient_noise(m,duration=0.2)
            #if(call==aname) :
            #print("listening....")
            audio=r.listen(m,timeout=7,phrase_time_limit=10)
            #r.pause_threshold=1
            text=r.recognize_google(audio)
            text=text.lower()
            print(text)
            return text
    except:
        if(call==aname):
            text="please, say it again"
            print("did not understood")
        pass
    return ""

def command1():
    r=sr.Recognizer()
    try:
        with sr.Microphone() as m:
            r.pause_threshold=1
            r.adjust_for_ambient_noise(m,duration=0.2)
            #if(call==aname) :
            print("listening....")
            audio=r.listen(m,timeout=7,phrase_time_limit=10)
            #r.pause_threshold=1
            text=r.recognize_google(audio)
            text=text.lower()
            print(text)
            return text
    except:
        text="please, say it again"
        print("did not understood")
        pass
    return ""




#text=command()
#speak(text)
#task(text)
def assistant():
    while True:
        print(".............")
        call=command()
        call=call.lower()
        #print(call)
        if(call==aname):

            speak("yes, please")
            print("+")
            work=command1()
        else:
            print("-")
            continue
        if(work!=''):
            task(work)
            call=''
            work=''

        else:
            speak('try again')
            print('try again')
            continue
speak("hey, i m "+aname+", your virtual assistant")
assistant()


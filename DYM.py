import datetime
import webbrowser as web
import pyttsx3 as pt
import speech_recognition as sr
import wikipedia as wp
import os
import random
from playsound import playsound as p

dev = pt.init('sapi5')
voices = dev.getProperty('voices')
dev.setProperty('voice', voices[2].id)


def asks():
    speak('Ask me something')


def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning Sir')
        speak('How are you?')
        asks()

    elif 12 <= hour < 18:
        speak('Good Afternoon Sir')
        speak('How are you?')
        asks()

    else:
        speak('Good Evening Sir')
        speak('How are you?')
        asks()


def speak(something):
    dev.say(something)
    dev.runAndWait()


'''
def noResponse():
    
    speak('You did not respond! Wanna say something?')
    query = ask().lower()
    if 'yes' in query:
        anythingElse()
    else:
        pass'''


def tryAgain():
    query1 = ask().lower()
    if ('yes' in query1) or ('yeah' in query1) or ('i do' in query1):
        doit()

    else:
        speak('Okay. Goodbye for now, sir!')
        pass


def anythingElse():
    speak('anything else?')
    query1 = ask().lower()
    if ('yes' in query1) or ('yeah' in query1) or ('i do' in query1):
        doit()

    else:
        speak('Okay. Goodbye for now, Sir!')
        pass


'''
def takeCommand():
    rec = sr.Recognizer()

    with sr.Microphone as source:
        rec.pause_threshold = 1
        audio = rec.listen(source)
    try:
        print('Recognizing...')
        query = rec.recognize_google(audio, language='en-in')
        return query

    except Exception as e:
        print(e)
        speak('I\'ve failed you, sir! Forgive me')

For future mail sending activity

def sendEmail(to, content):
     '''


def ask():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Go after you hear the beep')
        speak('GO!')
        # p('C:\\Users\\Dev\\Desktop\\project 4th sem\\go.mp3')
        print('Listening...')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            print('Recognizing...')
            query1 = r.recognize_google(audio, language='en-in')
            print(f'You: {query1}\n')
            return query1

        except Exception as e:
            print(e)
            ask()
            return "None"


if __name__ == '__main__':

    print('started!')

    def doit():
        query = ask().lower()

        if 'hi' in query or 'hello' in query:
            wish()

        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace('wikipedia', '')
                results = wp.summary(query, sentences=2)
                speak("According to wikipedia,")
                print(results)
                speak(results)
                anythingElse()

            except Exception as e:
                print(e)
                speak('MAYBE YOU SAID IT WRONG.. TRY AGAIN')
                tryAgain()

        elif 'open youtube' in query:
            web.open('youtube.com')
            anythingElse()

        elif 'open google' in query:
            web.open('google.com')
            anythingElse()

        elif ('open stack overflow' in query) or ('open stackoverflow' in query) or ('open stack over flow' in query):
            web.open('stackoverflow.com')
            anythingElse()

        elif 'open facebook' in query:
            web.open('facebook.com')
            anythingElse()

        elif 'on youtube' in query:
            query = query.replace('play', '')
            query = query.replace('on youtube', '')
            query = 'https://www.youtube.com/results?search_query=' + query
            web.open(query)
            anythingElse()

        elif 'play song' in query:
            music = 'C:\\Users\\Dev\\Desktop\\gaaa'
            songs = os.listdir(music)
            os.startfile(os.path.join(music, songs[0]))

            anythingElse()

        elif 'next song' in query:
            music = 'C:\\Users\\Dev\\Desktop\\gaaa'
            songs = os.listdir(music)
            os.startfile(os.path.join(music, songs[1]))
            anythingElse()

        elif ('stop' in query) and ('song' in query):
            os.system('cmd /c "taskkill/im Music.UI.exe"')
            speak('Music stopping right now!')
            anythingElse()

        elif 'time' in query:
            print(datetime.datetime.now().strftime('%H:%M:%S'))
            speak(datetime.datetime.now().strftime('%H:%M:%S'))
            anythingElse()

        elif 'code' in query:
            path = "C:\\Users\\Dev\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
            anythingElse()

        elif ('close browser' in query) or ('close web' in query):
            try:
                os.system('cmd /c "taskkill/im msedge.exe"')
                speak('browser closed sir!')
                anythingElse()
            except Exception as e:
                print(e)
                speak('I don\'t think I could do it sir. Do you want to try something else or try again?')
                tryAgain()

        elif ('shut down immediately' in query) or ('shutdown immediately' in query) or ('bye' in query):
            try:
                os.system('cmd /c "shutdown -s -t 60"')
                speak('Shutting down in 1 minute')
                anythingElse()

            except Exception as e:
                print(e)
                speak('Can\'t shutdown Do you want to try something else or try again?')

                tryAgain()

        elif ('search' in query) and (('in google' in query) or ('on google' in query)):
            try:
                query = query.replace('search', '')
                query = query.replace('in google', '')
                query = query.replace('on google', '')
                web.open('www.google.com/search?q=' + query)
                anythingElse()

            except Exception as e:
                print(e)
                speak('Couldn\'t understand that. Do you want to try again?')
                query1 = ask().lower()
                if ('yes' in query1) or ('yeah' in query1) or ('i do' in query1):
                    tryAgain()
                else:
                    speak('okay sir')
                    pass

        elif ('shut down' in query) or ('shutdown' in query):
            try:
                os.system('cmd /c "shutdown -s -t 1800"')
                speak(
                    'Good night... By the way I\'m sure Manu loves you as much as you do her. SLEEP TIGHT, SIR!')
                speak('Well I\'ll be up for some time')
                speak('You can cancel shutdown process if needed within 41 minutes. Say Shutdown immediately for '
                      'immediate shutdown')
                speak('Want me to put some music for you?')
                query2 = ask().lower()
                if ('yes' in query2) or ('yeah' in query2) or ('i do' in query):

                    playlist = ['https://www.youtube.com/watch?v=_zScs9cYWsw&ab_channel=minyu%EB%AF%BC%EC%9C%A0',
                                'https://www.youtube.com/watch?v=mJW57E7GpSo&ab_channel=Lily%27sCorner',
                                'https://www.youtube.com/watch?v=HGl75kurxok&ab_channel=Vangakuz%E3%83%B4%E3%82%A1%E3%83%B3%E3%82%AC%E3%82%AF%E3%82%BA',
                                'https://www.youtube.com/watch?v=y9YdkP-6d_E&list=RDMM&start_radio=1&rv=HGl75kurxok&ab_channel=AlbatrossNepal-Official']

                    web.open(random.choice(playlist))
                    anythingElse()

                    # web.open('https://www.youtube.com/watch?v=QN2RnjFHmNY&list=PLrHCSTtFkZZX4XeY059h0nwsmU3KKAVUh&index=1&ab_channel=KennyGVEVO')

                else:
                    speak('Have a good night sir')
                    pass

                anythingElse()

            except Exception as e:
                print(e)
                speak('Sorry sir! something seems wrong!')
                tryAgain()

        elif 'restart' in query:
            try:
                speak('RESTARTING...... well, in a minute')
                os.system('cmd /c "shutdown -r -t 60"')
                anythingElse()

            except Exception as e:
                print(e)
                speak('Sorry sir! something seems wrong!')
                tryAgain()

        elif 'cancel' in query:
            os.system('cmd /c "shutdown -a')
            speak('DONE SIR')
            anythingElse()

        elif 'exit' in query:
            os.system('cmd /c "taskkill/im pycharm64.exe"')

        elif 'sing song' in query:
            p('C:\\Users\\Dev\\Downloads\\sorry.mp3sfd ')
            anythingElse()

        else:
            speak('NOT WHAT I CAN DO RIGHT NOW. Do you want to try asking something else, sir?')
            tryAgain()

        '''
        For sending mail
        
        elif 'send email' in query:
            try:
                print('Tell me what to write:')
                speak('Tell me what to write:')
                content = takeCommand()
                to = "devendra.hamal058@gmail.com"
                sendEmail(to, content)
                speak('Email has been sent!')

            except Exception as e:
                print(e)
                print('Could not understand. Say that again!')
                speak('Could not understand. Say that again!')
        '''

    # wish()
    doit()

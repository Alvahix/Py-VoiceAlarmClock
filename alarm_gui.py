from tkinter import *
import webbrowser
from time import strftime
import pyowm
from threading import Timer
from decimal import *
from gtts import gTTS
import vlc
import time

root = Tk()

frame_1 = Frame(root, bg='gray')
frame_1.pack()


def what_location():
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="my-application")
    question_2 = Label(frame_1, text='WEATHER LOCATION:', bg='slategray', font=('centurygothic', 7))
    question_2.pack(fill=X)
    where = Entry(frame_1)
    where.pack(fill=X)

    def execute_loc(event):
        loc = where.get()
        location = geolocator.geocode(loc)
        lo = location.latitude
        la = location.longitude
        question = Label(frame_1, text='HOURS OF SLEEP', bg='slategray', font=('centurygothic', 7))
        question.pack(fill=X)
        time_ask = Entry(frame_1)
        time_ask.pack(fill=X)

        def entire_1():
            owm = pyowm.OWM('4c6c56c29073bc51f7a81b2af179fd97')
            observation = owm.weather_at_coords(lo, la)
            w = observation.get_weather()
            t = w.get_temperature('fahrenheit')
            t1 = round(t['temp'], 1)
            t1s = str(t1)
            obs = w.get_status()
            import win32com.client as wincl
            speak = wincl.Dispatch("SAPI.SpVoice")
            m = strftime('%H %M')
            if t1 >= 85:
                speak.Speak(
                    'Good Morning Alvah! The time is currently' + m + '. The weather outside is ' + t1s +
                    ' degrees and ' + obs + ' in ' + loc + '. You should wear something light, '
                    'it is hot out. Here is your morning news from N.P.R. Good luck on your interview!')
            elif 72.1 <= t1 <= 84.9:
                speak.Speak(
                    'Good Morning Alvah, The time is currently' + m + '. The weather outside is ' + t1s +
                    ' degrees and ' + obs + ' in ' + loc + '. You wont need a jacket, '
                    'but you may want shorts. Here is your morning news from N.P.R. Good luck on your interview!')
            elif 60 <= t1 <= 72:
                speak.Speak(
                    'Good Morning Alvah, The time is currently' + m + '. The weather outside is ' + t1s +
                    ' degrees and ' + obs + ' in ' + loc + '. You wont need a jacket. '
                    'Here is your morning news from N.P.R. Good luck on your interview!')
            elif 38 <= t1 <= 59.9:
                speak.Speak(
                    'Good Morning Alvah, The time is currently' + m + '. The weather outside is ' + t1s +
                    ' degrees and ' + obs + ' in ' + loc + '. You may want a light jacket. '
                    'Here is your morning news from N.P.R. Good luck on your interview!')
            elif 32 <= t1 <= 37.9:
                speak.Speak(
                    'Good Morning Alvah, The time is currently' + m + '. The weather outside is ' + t1s +
                    ' degrees and ' + obs + ' in ' + loc + '. You will want a winter coat. '
                    'Here is your morning news from N.P.R.')
            elif t1 <= 31.9:
                speak.Speak(
                    'Good Morning Alvah, The time is currently' + m + '. The weather outside is ' + t1s +
                    ' degrees and ' + obs + ' in ' + loc + '. It is below freezing, '
                    'so you will want a winter coat. Here is your morning news from N.P.R.')
            webbrowser.open('https://one.npr.org/')

        def entire(event):
            global alarm
            alarm = time_ask.get()
            alarm_string = str(alarm)
            alarm_str = Decimal(alarm)
            seconds_str = 3600 * alarm_str
            question.destroy()
            time_ask.destroy()
            from tkinter import messagebox
            messagebox.showinfo('Alarm Set', 'Alarm is set and will wake you up in ' + alarm_string + ' hours.')
            t = Timer(seconds_str, entire_1)
            t.start()
        root.bind('<Return>', entire)
    root.bind('<Return>', execute_loc)


set_alarm_photo = PhotoImage(file='set.png')
button_set = Button(frame_1, image=set_alarm_photo, bg='green', command=what_location)
button_set.pack()

root.mainloop()

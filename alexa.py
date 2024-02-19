#This code is just a test on how converting a data to sound works.
#In this case this is text to speech bcs first I want a version that works based on chatting with a bot.

from gtts import gTTS
import speech_recognition as sr
import os

r = sr.Recognizer()

my_Text = sr.AudioFile("audio_files_harvard.wav")
with my_Text as source:
    audio = r.record(source, duration=4)

text = r.recognize_google(audio)

test_sound = gTTS(text=text, lang="en", slow=True)

test_sound.save("test_Sound.mp3")

os.system("mpg321 test_Sound.mp3")

#text to speech programe in python 

from gtts import gTTS
import os

myText = "Artificial intelligence (AI) is a set of technologies that allow computers to perform tasks that mimic human cognitive functions"

language = 'en'

output = gTTS(text = myText, lang = language, slow = False)

output.save("output.mp3")

os.system("start output.mp3")
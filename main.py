from gtts import gTTS
import os # to open the mp3 file automatically we imported

#text = "Hello World How Are You !!" #text that we want to convert

abc = open("sample.txt")
text = abc.read()

language = "en" #the language what we use is English

obj = gTTS(text = text,lang=language,slow=False)

obj.save("sample.mp3") #the name of the mp3 file that we want to listen


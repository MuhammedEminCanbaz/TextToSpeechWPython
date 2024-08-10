from gtts import gTTS

text = "Hello World How Are You !!" #text that we want to convert

language = "en" #the language what we use is English

obj = gTTS(text = text,lang=language,slow=False)

obj.save("sample.mp3") #the name of the mp3 file that we want to listen


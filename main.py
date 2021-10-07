from gtts import gTTS

text = 'don\'t worry, be happy'
lang = 'en'

obj = gTTS(text=text, lang=lang, slow=True)
obj.save("welcome.mp3")


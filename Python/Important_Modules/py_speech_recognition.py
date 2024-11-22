# import speech_recognition as sr


# rec = sr.Recognizer()

# with sr.Microphone() as src:
#     print("Say Something")
#     rec.adjust_for_ambient_noise(src)
#     audio = rec.listen(src)

# try:
#     text = rec.recognize_sphinx(audio)
#     print(text)
# except sr.UnknownValueError:
#     print("Cant Recognize Audio")
# except sr.RequestError:
#     print("Error Happen")    
import pyttsx3
import speech_recognition as sr
from googletrans import Translator
import random

def speak(text):
    eng = pyttsx3.init()
    eng.setProperty("rate", 150)
    eng.setProperty("volume", 1)
    eng.say(text)
    eng.runAndWait()
def text(timeout=5,phrase_time_limit=7):
  recognizer=sr.Recognizer()
  with sr.Microphone() as source:
    greetings=["Speak, I'll translate","Go ahead, I'm listening","Say Something I'm ready"]
    a=random.choice(greetings)
    speak(a)
    try:
      audio=recognizer.listen(source,timeout=timeout,phrase_time_limit=phrase_time_limit)
    except sr.WaitTimeoutError:
      print("You did NOT say anything")
      return ""
  try:
    print("Recognizing Speech")
    text1=recognizer.recognize_google(audio,language='en-UK')
    print(f"You said {text1}")
    return text1
  except Exception as e:
    speak(e)
    return ""
def translate(text,target_language="es"):
  translator=Translator()
  translation=translator.translate(text,dest=target_language)
  print(f"Translated text: {translation.text}")
  return translation.text
def display():
  print("Available Languages-")
  print("1.Hindi(hi)")
  print("2.Tamil(ta)")
  print("3.Telugu(te)")
  print("4.Marathi(mr)")
  print("5.Gujarati(gu)")
  print("6.French(fr)")
  print("7.Malayalam(ml)")
  print("8.Punjabi(pa)")
  print("9.Bengali(bn)")
  print("10.German(de)")
  ch=int(input("Enter your choice:"))
  d={1:"hi",2:"ta",3:"te",4:"mr",5:"gu",6:"fr",7:"ml",8:"pa",9:"bn",10:"de"}
  return d.get(ch,"es")
def main():
  target_language=display()
  while True:
    original_text=text()
    if not original_text:
      continue
    if original_text.lower() in ["exist","stop"]:
      speak("Goodbye")
      break
  translated_text=translate(original_text,target_language)
  if translated_text:
    speak(translated_text,rate=130)

main()

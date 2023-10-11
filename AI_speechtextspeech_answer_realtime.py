import speech_recognition as sr
from bardapi import Bard
import os
from dotenv import load_dotenv
import pyttsx3
engine = pyttsx3.init()

load_dotenv()
token = os.getenv("BARD_API_KEY")

#apikey
bard = Bard('here')

recognition = sr.Recognizer()

#TH_voice_id -> XX_voice_id
TH_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_THAI" #you can input here \TTS_XXX

with sr.Microphone() as source:

    print("")
    print("")
    print("|| say HELLO.. ||")

    while True:
        audio = recognition.listen(source)

        try:
            text = recognition.recognize_google(audio, language='en')  # th -> en es

            if text == 'hello' :
                try:
                    print("")
                    print("=======================================================================")
                    print("")
                    print("| what your question? |")
                    print("")

                    audio_exam = recognition.listen(source)
                    text_exam = recognition.recognize_google(audio_exam, language='en')  #th -> en

                    print("your question is :", text_exam)

                    result= bard.get_answer(text_exam)['content']
                    print(result)

                    print("")
                    print("=======================================================================")
                    engine.setProperty('volume', 0.9)
                    engine.setProperty('rate', 160)

                    engine.setProperty('voice', TH_voice_id)  #XX_voice_id
                    engine.say(result)

                    engine.runAndWait()

                    print("")
                    print("")
                    print("|| say HELLO.. ||")

                except:
                    continue
        except:
            continue
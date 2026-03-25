import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak something...")
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
            return voice_data
        except sr.UnknownValueError:
            print("Welcome To My AI DESKTOP ASSISTANT")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

speech_to_text()

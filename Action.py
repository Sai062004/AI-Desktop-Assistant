import text_to_speech
import speech_to_text
import datetime
import webbrowser
import subprocess
import os
import sys
import platform

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        response = "My name is virtual assistant"
        
    elif "hello" in user_data or "hi" in user_data:
        response = "Hey sir, how can I help you?"
        
    elif "good morning" in user_data:
        response = "Good morning, sir."
        
    elif "what is the time" in user_data:
        current_time = datetime.datetime.now()
        response = f"Hour: {current_time.hour}, Minute: {current_time.minute}"
        
    elif "shutdown" in user_data:
        response = "Okay sir."
        print(response)

        if platform.system() =="Windows":
            os.system("shutdown /s /f /t 0")
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            os.system("suhtdown now")
        else:
            print("Unsupported operating system")
            sys.exit(1)
        
    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com/")
        response = "Now, you can enjoy your music."
        
    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        response = "YouTube is opened."
        
    elif "open google" in user_data:
        webbrowser.open("https://www.google.co.in/")
        response = "Google is now ready for you."
        
    elif "open whatsapp" in user_data:
        os.system("start whatsapp:")
        response = "WhatsApp Desktop has been opened."

    elif "open excel" in user_data:
        os.system("start excel")
        response = "Excel has been opened."

    elif "open word" in user_data:
        os.system("start winword")
        response = "Word has been opened."

    elif "open powerpoint" in user_data:
        os.system("start powerpnt")
        response = "PowerPoint has been opened."

    elif "open notepad" in user_data:
        os.system("start notepad")
        response = "Notepad has been opened."

    elif "open calculator" in user_data:
        os.system("start calc")
        response = "Calculator has been opened." 

    elif "open command prompt" in user_data:
        os.system("start cmd")
        response = "Command Prompt has been opened."

    elif "open chatgpt" in user_data:
        webbrowser.open("https://openai.com/chatgpt/")
        response = "ChatGPT is now ready for you."
        
    elif "open photos" in user_data:
        webbrowser.open("https://photos.google.com/")
        response = "Photos are opened; now enjoy the memories."
        
    elif "open mail" in user_data:
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        response = "Your mail has opened."
        
    elif "open contacts" in user_data:
        webbrowser.open("https://contacts.google.com/")
        response = "Your contacts have opened."
        
    else:
        response = "I am not able to understand."


    text_to_speech.text_to_speech(response)
    return response

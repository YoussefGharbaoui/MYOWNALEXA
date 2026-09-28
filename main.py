import speech_recognition as sr
import pyttsx3
from google import genai



def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """listens to microphone and returns text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            print(f"The audio has not been recognized")
            return
        except sr.RequestError:
            print("check your internet connection")
            return


def process_command(command):
    if "stop" in command or "exit" in command:
        speak("Shutting down.")
        return False
    elif "time" in command:
        # Code to fetch local computer time goes here
        speak("It is currently 10:50 PM.")
        return True

    # 2. THE AI BRAIN (For everything else)
    else:
        # If it's not a local command, send the text to your AI API
        speak("Let me think about that...")
        
        # Example API call (pseudo-code)
        # ai_response = ask_llm_api(command) 
        # speak(ai_response)
        
        return True
        
def main():
    speak("started.")
    running = True

    while running:
        user_text = listen()

        if user_text:
            running = process_command(user_text)


if __name__ == "__main__":
    main()

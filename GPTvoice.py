import speech_recognition as sr
from gtts import gTTS
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to convert text to speech
def speak(text):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")  # You may need to change this command based on your system's audio player

while True:
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Use the Google Web Speech API to recognize the audio
        text = recognizer.recognize_google(audio)
        print("You said:", text)

        # Check if the recognized text contains the keyword "Assisto"
        if "assistant" in text:
            response = "How can I help you?"
            print("assistant detected. Responding:", response)
            speak(response)

    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))
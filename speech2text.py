# Speech To Text — Python 
# Reference and documentation: https://venkatarangan.com/blog/2019/08/python-code-snippets-for-speech-in-tamil/

# pip install SpeechRecognition, pyaudio, setuptools

import speech_recognition as sr 

def speech_to_text():
    """
    Converts speech input in Tamil to text using the Google Speech Recognition API.

    1. This function uses the SpeechRecognition library to record audio from the microphone and convert it to text.
    2. It specifically recognizes speech in the Tamil language (ta-IN) using the Google Speech Recognition API.
    3. The speech_recognition library in Python does not require any API keys. 
    4. The function sends audio data to Google's servers and returns the transcribed text.
    5. Returns:
        WhatUSpoke: The text representation of the speech input in Tamil.
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something in Tamil and pause, no need to press any key")
        audio = r.listen(source)
        print("Got you")

    try:
        WhatUSpoke = r.recognize_google(audio, language="ta-IN")
        print("What you spoke (Google):", WhatUSpoke)
        return WhatUSpoke
    except:
        pass

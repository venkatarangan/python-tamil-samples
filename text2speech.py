# text to speech using gTTS library
# Reference and documentation: https://venkatarangan.com/blog/2019/08/python-code-snippets-for-speech-in-tamil/
# pip install gTTS 

import gtts as gt 
import os      

def text_to_speech(text, language, output_file):
    """
    Convert the given text to speech using gTTS library.
    
    This function uses the gTTS library to convert the provided text into speech.
    It specifically works for the given language (Tamil) using the Google Text-to-Speech (gTTS) API.
    The gTTS library in Python does not require any API keys.
    The function sends the data to Google's servers and saves the resulting audio file.

    Args:
        text (str): The text to be converted to speech.
        language (str): The language of the text, e.g., 'ta' for Tamil.

    Returns:
        None
    """
    tts = gt.gTTS(text=text, lang=language)
    tts.save(output_file)

# Use the operating system's default media player to play the 'Tamil-Audio.mp3' file
    os.system(output_file)

TamilText = "வணக்கம்.அறம் செய விரும்பு, ஆறுவது சினம், இயல்வது கரவேல், ஈவது விலக்கேல், உடையது விளம்பேல். நன்றி!"
text_to_speech(TamilText, 'ta', 'output-tamil-audio.mp3')
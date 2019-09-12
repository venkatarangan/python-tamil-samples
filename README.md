# Python-Samples

A set of quick samples that I wrote for the purpose of learning Python and playing around. There is no plan to make them any more useful, than as simple examples. Please treat them as as such. Surprisingly, some might be useful too, but that's an unintended consequence. 

[Venkatarangan Thirumalai](https://tncv.me)

## Speech to Text: ##
I got the base code from [here](https://medium.com/@rahulvaish/speech-to-text-python-77b510f06de). You need to install [SpeechRecognition package](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio), available through PIP and PyAudio (available through PIP in Linux, but on Windows, you need to install appropriate [package from here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).

## Text to Speech: ##
When I posted the above code, I got a reader request for a code that does the reverse – to speak out loud a sentence of given Tamil text. I have given this below. I got the base [code from here](https://www.thecrazyprogrammer.com/2018/05/python-text-to-speech.html). You need to install [gTTS package](https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang), available through PIP. The code uses os.system to play the output audio file, this command works out of the box in Windows, in Linux you may need a command-line player like MPG321 (which can be installed using *sudo apt-get install mpg321*)

You can listen to the output audio that’s produced by the code above, [here](https://soundcloud.com/venkatarangan-thirumalai/tamil-first-fivee-of-athisudi). 

The above were possible, thanks, to the numerous readymade packages that are available for free, and, the magic of cloud – in these two cases I am using Google Cloud, which required no configuration or key for trial runs. You may use Bing if you have an Azure API key.


# Python-Tamil-Samples

## Overview

A set of quick samples that I wrote for the purpose of experimentations using Python language on handling Tamil text. These were written around 2019. 

Details are in the following blog posts:
 1. Python and Google Cloud Vision for Tamil text [https://venkatarangan.com/blog/2019/09/python-and-google-cloud-vision-for-tamil-text/]

 1. Tools and Applications in Tamil [https://venkatarangan.com/blog/2019/09/tools-applications-available-for-tamil/]

 1. Python code snippets for Speech in Tamil [https://venkatarangan.com/blog/2019/08/python-code-snippets-for-speech-in-tamil/]

## Disclaimer

These are simple examples and trials. Please treat them as as such. Some might be useful too, but that's an unintended consequence. 

## Recent Updates

While randomly checking my GitHub account on 25 May 2024, I came across this repository and noticed it lacked basic context and comments, I have added the same and made the repository public.

## License

This project is licensed under the MIT License.

## Contributions

This project was an experiment and is not maintained. Just take it as it is. Thanks.

## Author

Venkatarangan Thirumalai [venkatarangan.com](https://venkatarangan.com)

# Samples available here: #
## Speech to Text: ##
I got the base code from [here](https://medium.com/@rahulvaish/speech-to-text-python-77b510f06de). You need to install [SpeechRecognition package](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio), available through PIP and PyAudio (available through PIP in Linux, but on Windows, you need to install appropriate [package from here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).

## Text to Speech: ##
In 2019, when I posted the speech to text code, I got a reader request for a code that does the reverse – to speak out loud a sentence of given Tamil text. I got the base [code from here](https://www.thecrazyprogrammer.com/2018/05/python-text-to-speech.html). You need to install [gTTS package](https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang), available through PIP. The code uses os.system to play the output audio file, this command works out of the box in Windows, in Linux you may need a command-line player like MPG321 (which can be installed using *sudo apt-get install mpg321*)
You can listen to the output audio that’s produced by the code in the sample output MP3 file titled: **output-tamil-audio.mp3**.

The above were possible, thanks, to the numerous readymade packages that are available for free, and, the magic of cloud – in these two cases I am using Google Cloud, which required no configuration or key for trial runs. You may use Bing if you have an Azure API key.

## Vision and Translate ## 
This is a Quick 'n' Dirty code snippet that uses Google Cloud Vision OCR to extract the Tamil text from a given image containing Tamil text, then uses Google Cloud Translate to translate the Tamil text to English. The text parsing needs a lot more work to be better. 

Tamil Text present in the image file as recognized by the Cloud Vision OCR: 
~~~~
புதிய இடத்தில் அதெல்லாம் பலிக்குமா?
பெரியவர் ஆறுமுகத்தோடு மல்லிகா நாகப்பட்டினத்
தில் கப்பலேறியபோது வழியனுப்ப வந்தவர்கள் வாய்
வார்த்தையின்றி அழுதழுது கண்ணைக் கடலாக்கிக்
கொண்டார்கள்.
அவர்களை அவள்தான் தேற்ற வேண்டியிருந்தது
"மாமாவின் கடைசி ஆசையை நான் நிறைவேற்ற
வேண்டாமா? அந்த ஆத்மாவுக்குச் சாந்தி கிடைக்க
வேண்டாமா? கோடை விடுமுறையில் தானே போகிறேன்.
~~~~
The output English translation:

~~~~
Will it be sacrificed in the new place? When Mallika sailed to Nagapattinam with the eldest, the passersby cried without a word. &quot;Do I not fulfill my uncle&#39;s last wish? Do I not find peace with that soul? I am going on summer vacation.
~~~~

## Tamil Letters Count ##
This project uses the [Grapheme](https://github.com/alvinlindstam/grapheme) package, which is a wonderful package to perform string operations on language recognized characters. 

In 2004, when I faced the issue of counting of number of characters for a given Tamil string, the standard library functions were not useful for non-latin scripts, so  I had to [write a paper for a conference and submitted code written in .NET, Perl and VB.NET](https://venkatarangan.com/blog/2004/12/counting-letters-in-an-unicode-string/) to solve this problem, specific for Tamil. Now, Grapheme makes it super easy and is updated upto Unicode 12.0.0 standard. 
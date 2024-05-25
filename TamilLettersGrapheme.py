# Reference and documentation: https://venkatarangan.com/blog/2019/09/tools-applications-available-for-tamil/ 
# pip install grapheme

import grapheme

def tamil_letters_grapheme():
    """
    This script demonstrates the usage of the grapheme library to work with Tamil letters.
    It calculates the number of letters in a Tamil string and also uses grapheme to handle grapheme clusters.

    Tamil string: அம்மா என்றால் அழகு, என் தாய் முத்துலட்சுமி என்று சொன்னான் முருகன்
    Tamil string 2: தமிழ்நாடு

    Output:
    - Number of letters in the Tamil string using standard Python len function
    - Number of grapheme clusters in the Tamil string using the grapheme library
    - First 8 characters of the Tamil string using standard Python string slicing
    - First 8 characters of the Tamil string with grapheme clusters
    """

    தமிழ்வரி = "அம்மா என்றால் அழகு, என் தாய் முத்துலட்சுமி என்று சொன்னான் முருகன்"
    NumOfLetters = len(தமிழ்வரி)
    print("Standard len count for: ", தமிழ்வரி, ":", NumOfLetters)

    gl = grapheme.length(தமிழ்வரி)
    print("Grapheme count for", ":", தமிழ்வரி, ":", gl) 

    print("First 8 characters with outofbox function: ", தமிழ்வரி[0:7])
    glslice = grapheme.slice(தமிழ்வரி, 0, 8)
    print("First 8 characters with Grapheme: ", glslice)

    #Unicode values for the string "தமிழ்நாடு"
    தமிழ்வரி2 = "\u0BA4\u0BAE\u0BBF\u0BB4\u0BA8\u0BBE\u0BA9\u0BC1"
    NumOfLetters = len(தமிழ்வரி2)
    print("Standard len count for: ", தமிழ்வரி2, ":", NumOfLetters)
    gl2 = grapheme.length(தமிழ்வரி2)
    print("Grapheme count for", ":", தமிழ்வரி2, ":", gl2) 

tamil_letters_grapheme()

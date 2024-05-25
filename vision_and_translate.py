#Reference and documentation: https://venkatarangan.com/blog/2019/09/python-and-google-cloud-vision-for-tamil-text/ 

#pip install google-cloud-vision
#pip install google-cloud-translate
#You need to create your own client_secrets.json from Google Cloud Platform. The file in this project is an empty one.

def detect_text(path):
    """
    Detects text in an image using the Google Cloud Vision API.

    Args:
        path (str): The path to the image file.

    """
    from google.cloud import vision
    import os
    import io

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "client_secrets.json"
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.text_detection(
        image=image,
        image_context={"language_hints": ["ta"]},  # Tamil
    )
    texts = response.text_annotations
    return texts
# [END vision_text_detection]

#pip install google-cloud-translate

def Quick_Translate(SourceText):
    from google.cloud import translate

    # Instantiates a client
    translate_client = translate.Client()

    sourcelanguage = 'ta'
    targetlanguage = 'en'

    translation = translate_client.translate(
        SourceText,
        source_language=sourcelanguage,
        target_language=targetlanguage)

    return translation['translatedText']
# [END translate_quickstart]

path = 'input_tamil_page.jpg'

mytexts = detect_text (path)
mytext = mytexts[0].description
print (mytext)

mytranslated = Quick_Translate (mytext)
print (mytranslated)

#you can view the sample output in the output_vision_and_translate.txt file in the same folder.
import re
from PIL import ImageGrab
import pytesseract
from typing import List
from collections import Counter


def capture_and_read():
    # Capture whole screen
    screenshot = ImageGrab.grab()
    filepath = "C:\\Users\\danedens\\Pictures\\temp.jpg"
    screenshot.save(filepath)
    # You might need to convert the screenshot to grayscale or apply other transformations for better OCR
    screenshot = screenshot.convert('L')

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(screenshot)
    print(text)
    return text





def clean_text_and_find_duplicates(text: str) -> List[str]:

    """

    Function to clean up the text into an array, and then prints any duplicate words



    :param text: input text

    :type text: str

    :return: list of duplicate words

    :rtype: List[str]

    """

    # Replace non-word characters (anything other than a letter, digit or underscore) with a space

    cleaned_text = re.sub(r'\W', ' ', text)



    # Convert the text to lowercase and split it into words

    words = cleaned_text.lower().split()



    # Count the occurrences of each word

    word_counts = Counter(words)



    # Find the words that appear more than once and return them

    duplicates = [word for word, count in word_counts.items() if count > 1]

    

    return duplicates

print(clean_text_and_find_duplicates(capture_and_read()))

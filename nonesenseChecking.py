from langdetect import detect, DetectorFactory
import re
from nltk.corpus import words

# for streamlit -- because mawala sa iyaha si words | web hosting purposes
import nltk
nltk.download('words')


class InputChecker:
    def __init__(self):
        self.valid_words = set(words.words())  # Load valid words
        DetectorFactory.seed = 0  # For consistent results

    # Checking if gibberish like asdsacaewefhj
    def is_nonsensical_input(self, user_input):
        DetectorFactory.seed = 0  # For consistent results

        # Check if the input consists of gibberish or random letters
        if re.match(r'^[a-z]+$', user_input) and len(user_input) > 5:
            return True

        # Check for too many consecutive consonants or vowels
        if re.search(r'(?i)([bcdfghjklmnpqrstvwxyz]{4,}|[aeiou]{4,})', user_input):
            return True

        # Check if the input is not in the dictionary of valid words
        valid_words = set(words.words())  # Load valid words
        input_words = user_input.split()  # Split input into words

        # Check if all words are not in valid words
        if all(word not in valid_words for word in input_words):
            return True

        # Language detection
        try:
            lang = detect(user_input)
            if lang != 'en':
                return True
        except:
            pass  # Handle cases where detection fails

        return False


    # Checking if math ba siya
    def is_mathematical_expression(self, user_input):
        # Check if the input is a mathematical expression
        return re.match(r'^[\d\s\+\-\*\/\%\(\)]+$', user_input.strip()) is not None
    

    # Remove punctuations
    def remove_punctuation(self, text):  # removes punctuations
        return re.sub(r'[^\w\s]', '', text)
import string


def is_pangram(sentence):
    # ALPHABET = set(string.ascii_lowercase)
    # return ALPHABET.issubset(sentence.lower())
    lower_alphabets = set(sentence.lower())
    for i in lower_alphabets:
        if not 96 <= ord(i) <= 122:
            return False
    return True

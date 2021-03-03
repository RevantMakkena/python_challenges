

# %% naive approach  O(n)
import string


def is_pangram(sentence):
    target_list = []
    for i in range(26):
        target_list.append(False)

    # Loop through each character
    for c in sentence.lower():
        if not c.strip() == "":  # To trim a character for spaces
            # Ord return integer value (unicode equivalence)
            target_list[ord(c)-ord('a')] = True

    # Check for any falsey value
    for i in target_list:
        if target_list[i] == False:
            return False

    return True


is_pangram("the quick brown fox jumps over the lazy dog")

# %% naive app 2

# This won't work, no way to tell if all alphabets have been satisfied or not


def is_pangram(sentence):
    all_alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for i in sentence:
        if not i.strip() == "" and i not in all_alphabets:
            return False
    return True


is_pangram("the quick brown fox jumps over the lazy dog")

# %%
# Set equality operator compares if there are same elements or not. so this would work


def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    return set(sentence.lower()) >= alphabet


# is_pangram("the quick brown fox jumps over the lazy dog")
x = is_pangram('the quick brown fox jumps over the lazy dog')
print(x)

# %%
# IsSubset reports whether another set contains this set


def is_pangram(sentence):
    ALPHABET = set(string.ascii_lowercase)
    return ALPHABET.issubset(sentence.lower())


# %% Subtracting will remove elements that matched

ALPHABET = set(string.ascii_lowercase)


def is_pangram(sentence):
    return not ALPHABET-set(sentence.lower())
# %%

# Check if each character of the string lies between the ASCII range of lowercase alphabets i.e. 96 to 122.
# but still gotchas like not all characters available and all that


def is_pangram(sentence):
    lower_alphabets = set(sentence.lower())
    for i in lower_alphabets:
        if not 96 <= ord(i) <= 122:
            return False
    return True

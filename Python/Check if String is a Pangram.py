import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    return set(sentence.lower()) >= alphabet

user_input = input("Enter a sentence: ")
if is_pangram(user_input):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")

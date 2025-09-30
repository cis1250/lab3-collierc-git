#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

while True:
    user_sentence = input("Enter a sentence: ")
    if is_sentence(user_sentence):
        break

list1 = user_sentence.split(' ')
list2 = set(list1)
list3 = []*len(list2)

for words in list2:
    list2[words] = 0

for words in list1:
    list3[list2.index(words)] += 1

for words in list2
    print(words + ":")
    print(list3[list2.index(words)])

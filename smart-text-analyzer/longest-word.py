

def longest_word_in_sentence(sentence):
    words = sentence.split()
    longest = max(words, key=len, default="")
    return longest

sentence = input("Enter a sentence: ")
result = longest_word_in_sentence(sentence)
print(f"The longest word is: {result}")

def longest_word_in_list(word_list):
    longest = max(word_list, key=len, default="")
    return longest

words = ["apple", "banana", "cherry", "banana"]
result = longest_word_in_list(words)
print(f"The longest word is: {result}")


import re

def longest_word_advanced(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower())
    return max(words, key=len, default="")
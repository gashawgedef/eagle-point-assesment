def calculate_total_characters(text):
    return len(text)

def calculate_total_words(text):
    words = text.split()
    return len(words)

def calculate_average_word_length(text):
    words = text.split()
    total_characters = sum(len(word) for word in words)
    average_length = total_characters / len(words)
    return average_length

def find_most_frequent_character(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            char_count[char] = char_count.get(char, 0) + 1
    most_frequent_char = max(char_count, key=char_count.get)
    return most_frequent_char, char_count[most_frequent_char]

def find_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word

# Get input from the user
user_input = input("Enter a text: ")

# Perform calculations and display results
total_characters = calculate_total_characters(user_input)
total_words = calculate_total_words(user_input)
average_word_length = calculate_average_word_length(user_input)
most_frequent_char, frequency = find_most_frequent_character(user_input)
longest_word = find_longest_word(user_input)

print(f"Entered text was: {user_input}")
print(f"Total characters: {total_characters}")
print(f"Total words: {total_words}")
print(f"Average word length: {average_word_length}")
# print(f"Most frequent character: {most_frequent_char} (frequency: {frequency})")
# print(f"Longest word: {longest_word}")
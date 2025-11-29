# Eagle point Assesment Documentations
**Name:** Gashaw Gedef
## TASK 1: Smart Text Analyzer

### 1. Searches Performed (exact queries + URLs)




**Query:** "Write a `python` fumction to count words in text"
### URLs and Solutions
https://www.geeksforgeeks.org/python/python-program-to-count-words-in-text-file/
https://stackoverflow.com/questions/19410018/how-to-count-the-number-of-words-in-a-sentence-ignoring-numbers-punctuation-an
https://thegeekycodes.com/building-a-python-word-counter-and-analyzer/
https://code.tutsplus.com/counting-word-frequency-in-a-file-using-python--cms-25965t
https://www.kaggle.com/code/saidrahmatpanah/lab3-6-text-analysis
https://advertools.readthedocs.io/en/master/advertools.word_frequency.html

- 1 use `split()`

```
c=0
with open(r'C:\Users\ggashaw\Desktop\sample_file.txt','r') as file:
    data= file.read()
    lines =data.split()
    for word in lines:
        if not word.isnumeric():
            c+=1

print(c)
```
input text

```
welcome, to ethiopia as todat good as goof df gh jk ?
```
**output:**

![](/images/count1.PNG)
from the result we can understand that panctuation is counted as a word when we use `split()` method.

- 2 use Regular Exprestion to get Word Count
```

import collections
import re
from collections import Counter


def count_words(text):
    words = re.findall(r'\w+',text.lower())
    return words

"Analyzing word frequency"
def analyze_word_frequency(words):
    word_count=collections.Counter(words)
    return word_count


def main():
    filename =  r"C:\Users\ggashaw\Desktop\sample_file.txt"
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            words = count_words(text)
            print("words count:",len(words))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()
```
***Output:**
![](/images/count2.PNG)

The above reregular expression  excludes `panctuations` to be counted as a word and the number of words in a text is `11`. it solves the problem identified when using `split()` method. 

**Query:** "Write a `python` fumction to find  average Word Length in text"
### URLs and Solutions
https://stackoverflow.com/questions/28333732/how-to-calculate-average-word-sentence-length-in-python-2-7-from-a-text-file
https://medium.com/data-and-beyond/build-python-project-a-text-analyzer-tool-686c9647a54c
https://www.daniweb.com/programming/software-development/threads/194704/average-word-count-in-a-text
https://www.kaggle.com/code/iamrahulthorat/assignment-6-sample-solution
https://www.geeksforgeeks.org/python/python-average-string-length-in-list/
https://www.digitalocean.com/community/tutorials/average-of-list-in-python
https://www.geeksforgeeks.org/python/python-average-string-length-in-list/

to find the Average of length of words in text:

```
def average_word_length(text):
    words = text.split()
    total_length = 0
    for word in words:
        total_length += len(word)

    average_length = total_length / len(words)
    return average_length
```
***Output:**
![](images/count3.PNG)
From above code the result is `5.66666666667` not in 2 decimal places. 

**Query:** "Write a `python` fumction to find  the longest word in Text or list "
### URLs and Solutions

https://stackoverflow.com/questions/16365807/finding-the-longest-words-in-a-text-file
https://www.geeksforgeeks.org/python/python-program-to-find-the-longest-word-in-a-sentence/
https://systechgroup.in/blog-python-program-to-find-the-longest-word/
https://www.geeksforgeeks.org/dsa/find-the-length-of-the-longest-possible-word-chain/

- sample code 

```
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

words = ["apple", "banana", "cherry", "Telecommunications"]
result = longest_word_in_list(words)
print(f"The longest word is: {result}")


import re

def longest_word_advanced(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower())
    return max(words, key=len, default="")

```

**Query:** "Write a `python` fumction to find  word frequency in text or list "
### URLs and Solutions

https://thegeekycodes.com/building-a-python-word-counter-and-analyzer/
https://stackoverflow.com/questions/35857519/efficiently-count-word-frequencies-in-python
https://www.geeksforgeeks.org/python/find-frequency-of-each-word-in-a-string-in-python/


```
def analyze_word_frequency(words):
    # Count word occurrences
    word_count = collections.Counter(words)
    return word_count
```
we analyze the `frequency` of each word using the collections.Counter function.


## Final Solution for Task 1
### Thought Process & Decisions 
- First  used the method  `text.split()`  and  fails on punctuation ("?" counted as a word)
- when using above `text.split()` method, it requires many for loops which may lead to errors and difficult to read
- Used regular pattern  `re.findall(r'\w+', text.lower())` to extract clean words
- Used `collections.Counter` standard library  to get the frequency of word easily.
- to get  Average length: simple sum of lengths divided by count, round to 2 decimal place is required

**Why You choose this approach?**
- I considered Time and Space complexity to O(n)
- The this ext solution should handle panctuations 
- The code should be easily readable and maintainable

**Steps to Implement Task One**

- 1. Use regex to extract words in text   like `re.findall(r'\w+', text.lower())`
- 2. count the length of words in text using the method   `len(words)`
- 3. Calculate total characters a word contains in a text
- 4. Find average word length and round to 2 decimal places
- 5. Find The longest word in list of words
- 6. count frequency of word in text
- 7. Wrappe  everything in one function and return in the required format


**Task 2:** Async Data Fetcher with Retry (JavaScript) 
**Task 3:** Rate Limiter (Python)  
**Date Submitted:** 29 November 2025

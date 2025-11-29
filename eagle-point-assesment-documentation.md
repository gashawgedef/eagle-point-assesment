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

![](/images/count1.png)
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
![](/images/count2.png)

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


**Task 2:** Async Data Fetcher with Retry (JavaScript) 
**Task 3:** Rate Limiter (Python)  
**Date Submitted:** 29 November 2025

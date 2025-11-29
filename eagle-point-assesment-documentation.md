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

use `split()`

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

![]("/images/count1.png")

**Task 2:** Async Data Fetcher with Retry (JavaScript) 
**Task 3:** Rate Limiter (Python)  
**Date Submitted:** 29 November 2025

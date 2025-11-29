import re
frequency = {}
document_text = open('C:\Users\ggashaw\Desktop\sample_file.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
blacklisted = ['the', 'and', 'for', 'that', 'which']
 
for word in match_pattern:
    if word not in blacklisted:
        count = frequency.get(word,0)
        frequency[word] = count + 1
most_frequent = dict(sorted(frequency.items(), key=lambda elem: elem[1], reverse=True))
most_frequent_count = most_frequent.keys()
 
for words in most_frequent_count:
    print(words, most_frequent[words])
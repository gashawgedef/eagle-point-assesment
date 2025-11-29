
import collections
import re

def smart_text_analyzer(text):
    words = re.findall(r'\w+',text.lower())
    if not words:
        return {
            "word_count": 0,
            "average_word_length": 0.00,
            "longest_words": [],
            "word_frequency": {}
        }
    word_count=len(words)
    total_characters = sum(len(word) for word in words)
    average_length = round(total_characters / word_count, 2)
    longest_word = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == longest_word]
    word_frequency =dict(collections.Counter(words))
    
    return  {
        "word_count": word_count,
        "average_word_length": average_length,
        "longest_words": longest_words,
        "word_frequency": word_frequency
    }



if __name__ == "__main__":
    example = "Ethiopia, the cradle of humanity,  Gondar’s castles."
    result = smart_text_analyzer(example)
    
    import json
    print(json.dumps(result, indent=4))



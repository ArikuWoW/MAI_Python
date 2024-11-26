import collections
import re

def count_unique_words(text):
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()
    word_counts = collections.Counter(words)
    unique_words_count = len(word_counts)
    return unique_words_count

example_text = "Hello, world! This is a test. Hello, world!"
print(count_unique_words(example_text))

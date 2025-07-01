import nltk
from nltk.corpus import words

try:
    nltk.data.find('corpora/words')
except LookupError:
    nltk.download('words')

word_list = set(words.words())

def is_common_word(password: str) -> bool:
    return password.lower() in word_list

# ...existing code...

if __name__ == "__main__":
    test_word = "password"
    print(f"Is '{test_word}' a common word? {is_common_word(test_word)}")
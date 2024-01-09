# Normalization is about making texts uniform
import re
# pip install nltk
from nltk.tokenize import word_tokenize, sent_tokenize
text = "In a deep dark forest, there are 10 wolves, 2 bears, and 1 bunny who ruled them all."


text = text.lower()

def normalize(input_str):
    input_str = input_str.lower()
    # Selecting anything that is Not alphanumeric characters or the whitespace
    pattern = r"[^\w ]"
    # Removed all special characters
    return re.sub(pattern, '', input_str)

# Tokenization
longer_text = "Regular Expression is a sequence of characters that defines a search pattern. It is used for matching and manipulating strings, typically within text or character data. Regular expressions provide a flexible and efficient way to search, match, and manipulate text based on certain patterns."

word_tokens = word_tokenize(normalize(longer_text))
# print(word_tokens)
# print(sent_tokenize(longer_text))

with open("textfile.txt", "r") as f:
    content = f.read()
    # print(word_tokenize(normalize(content)))

# Removing Stopwords
# Before this line, run these two lines!
# import nltk
# nltk.download('popular')
from nltk.corpus import stopwords

english_stop_words = set(stopwords.words('english'))
# print(english_stop_words)

# Creating a list of words in word_tokens that does not belong in english_stop_words set
filtered = [w for w in word_tokens if not w in english_stop_words]
# print(filtered)

from nltk.book import text1, text5

# findall https://www.nltk.org/api/nltk.text.html
text5.findall("(<.*><.*>)<bro>")
text1.findall("<a><.*><boat>")

# collocations
text1.collocations()

# concordance returns all context the word "white" was used in
text1.concordance('monstrous')

# similar returns words that were used in similar context to word "monstrous"
text1.similar('monstrous')
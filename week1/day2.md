# Week 1 - Day 2: Introduction to Natural Language Processing (NLP) and Regular Expressions

## Agenda

1. **Introduction to NLP:** Understanding the basics of Python programming language.
2. **Introduction to Regular Expressions:** Learn about the basics of regular expressions, their syntax, and how to use them in Python for pattern matching in text.
3. **Hands-on Session:** Practical exercises to apply the concepts learned.

## Learning Objectives

By the end of this session, you should be able to:

- Understand the basics of Natural Language Processing.
- Understand the concept of regular expressions and how to use them for pattern matching in Python.

---

## Introduction to Natural Language Processing (NLP)

Natural Language Processing, or NLP, is a field that focuses on enabling computers to understand and use human language. It's a key tool in extracting insights from text data. Here are some of the key areas and applications of NLP:

- **Text Classification:** This involves sorting news articles into different topics or categories.

- **Sentiment Analysis:** This technique is used to determine whether customer reviews are positive or negative.

- **Named Entity Recognition (NER):** This can identify specific names or places in documents.

- **Language Translation:** This involves converting text from one language to another, making it easier to communicate between different languages.

In addition to these, we have powerful tools like Hugging Face Transformers. This library provides pre-trained models for a wide range of NLP tasks, including language translation, text generation, and sentiment analysis. It is built on top of PyTorch and TensorFlow and is known for its user-friendly API.

However, NLP faces several challenges. Human languages are complex and constantly evolving, making it difficult for computers to keep up. NLP strives to bridge this gap.

---

## Introduction to Regular Expressions

Regular expressions are powerful tools used in programming to search, match, and manipulate text. They are primarily used for data validation and text processing.

### Why Learn Regular Expressions?

Regular expressions are great for handling text data. They can:

- Find specific text patterns
- Check if data is in the right format
- Organize large amounts of text data

### Real-World Applications

#### General Use Cases

- Validating data formats (email, phone number, password, etc.)

#### Use Cases in Machine Learning and NLP

- **Data Cleaning in Text Classification:** Regular expressions can remove unnecessary characters from text.
- **Named Entity Recognition (NER) Preprocessing:** They can help in finding names or other specific entities in text.
- **Tokenization:** Regular expressions can break text into smaller parts, like sentences or words, for analysis.

---

## Natural Language Toolkit (NLTK)

NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources.

### Key Concepts

- **Normalization:** This process makes text uniform for analysis. It's about making the text consistent. For example, converting all words to lowercase, removing punctuation, and standardizing different spellings of the same word.

- **Tokenization:** This involves breaking text into smaller parts called tokens. Tokens can be words, phrases, or other meaningful units. For instance, "I love NLTK!" becomes ["I", "love", "NLTK", "!"]. This is crucial for detailed text analysis.

### NLTK Examples

#### Normalization

Let's first normalize the text by making everything lower case and removing punctuations using regex. The pattern \W will match any character that is not alphanumeric.

```python
import re

text = "If a quick, brown fox jumps! over the lazy cat and takes- a long nap themselves... does that make the fox itself lazy?"

# Convert all text to lower case
text = text.lower()

# Write a regex that matches all non-alphanumeric characters
pattern = r"\W"

# Replace all matches with white spaces
normalized = re.sub(pattern, ' ', text)

print(normalized)
```

#### Tokenization

Next, we break each word into a token.

```python
from nltk.tokenize import word_tokenize

word_tokens = word_tokenize(normalized)

print(word_tokens)
```

#### Stopwords

We can remove common words that do not offer a lot of meaning or context, such as "the", "this", "in".

```python
from nltk.corpus import stopwords

# Create a set of NLTK's English stopwords
stop_words = set(stopwords.words('english'))

# Remove stopwords from the tokenized text
filtered = [w for w in word_tokens if not w in stop_words]

print(filtered)

# Output: ['quick', 'brown', 'fox', 'jumps', 'lazy', 'cat', 'takes', 'long', 'nap', 'make', 'fox', 'lazy']
```

### Text Analysis Example

#### FindAll

FindAll function finds instances of the regex in the text. The text is a list of tokens. The regex must be surrounded by angle brackets.

```python
from nltk.book import text1, text5

# finds 2 tokens that precedes the word "bro"
text5.findall("<.*><.*><bro>")

# Output: you rule bro; telling you bro; u twizted bro

# finds the token that is between the word 'a' and the word 'man', essentially returning adjectives describing a man.
text1.findall("<a>(<.*>)<man>")

# Output: monied; nervous; dangerous; white; white; white; pious; queer; good; mature; white; Cape; great; wise; wise; butterless; white; fiendish; pale; furious; better; certain; complete; dismasted; younger; brave; brave; brave; brave
```

### Concordance

Concordance shows the context where a specified word appears.

```python
from nltk.book import text1

text1.concordance('monstrous')

"""
Displaying 11 of 11 matches:
ong the former , one was of a most monstrous size . ... This came towards us ,
ON OF THE PSALMS . " Touching that monstrous bulk of the whale or ork we have r
ll over with a heathenish array of monstrous clubs and spears . Some were thick
d as you gazed , and wondered what monstrous cannibal and savage could ever hav
that has survived the flood ; most monstrous and most mountainous ! That Himmal
they might scout at Moby Dick as a monstrous fable , or still worse and more de
th of Radney .'" CHAPTER 55 Of the Monstrous Pictures of Whales . I shall ere l
ing Scenes . In connexion with the monstrous pictures of whales , I am strongly
ere to enter upon those still more monstrous stories of them which are to be fo
ght have been rummaged out of this monstrous cabinet there is no telling . But
of Whale - Bones ; for Whales of a monstrous size are oftentimes cast up dead u
"""
```

### Similar

The similar function returns words that appear in the same context as the provided word.

```python
from nltk.book import text1

# There's a typo in 'monstorous', it should be 'monstrous'
text1.similar('monstrous')

# Output: true contemptible christian abundant few part mean careful puzzled mystifying passing curious loving wise doleful gamesome singular delightfully perilous fearless
```

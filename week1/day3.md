# Week 1 - Day 3: Introduction to Python Word Embeddings

## Agenda

1. **Introduction to NLP:** Understanding the basics of Python programming language.
2. **Introduction to Regular Expressions:** Learn about the basics of regular expressions, their syntax, and how to use them in Python for pattern matching in text.
3. **Hands-on Session:** Practical exercises to apply the concepts learned.

## Learning Objectives

By the end of this session, you should be able to:

- Understand the basics of Natural Language Processing.
- Understand the concept of regular expressions and how to use them for pattern matching in Python.

---

## Word2Vec, GloVe

### Word Embeddings in NLP: Word2Vec and GloVe

Word embeddings are techniques that convert words into numerical representations (vectors). This helps us understand the meaning and relationships between words. For example, "dog" and "cat" will have vectors that show they are related, unlike "dog" and "fire".

#### Word2Vec

Word2Vec is a technique that suggests words with similar contexts have similar meanings. It has two architectures:

- Continuous Bag of Words (CBOW): This predicts a word based on its surrounding context.
- Skip-gram: This predicts surrounding context words given a target word. For example, in the sentence: "The cat sat on the mat." If we choose "sat" as the target word, Skip-gram will try to predict the context words ("The", "cat", "on", "the").

The main point of Word2Vec is it focuses on words' local context.

#### GloVe (Global Vectors for Word Representation)

GloVe is similar to Word2Vec in creating word vectors, but it works differently. It keeps track of how frequently words show up together in the whole text. This method helps us understand how words are used throughout the entire text, not just nearby each other.

### Word2Vec Example

Explore Word2Vec features using a pretrained model from Gensim, trained on the Google News dataset (approx. 100 billion words).

```python
# Load the pretrained Word2Vec model
import gensim.downloader as api

w2v = api.load('word2vec-google-news-300')
```

#### Displaying Common Words

```python
# Print the most common words in the model
print(f"Total words in model: {len(w2v.index_to_key)}")

for index, word in enumerate(w2v.index_to_key):
    if index < 10:
        print(f"Word #{index + 1}: {word}")
```

#### Word Vector Representation

```python
# Retrieve the vector representation of a word

vec_computer = w2v['computer']

print("Vector for 'computer':\n", vec_computer)
```

#### Handling Unknown Words

```python
# Attempting to access a vector for an unknown word

try:
    w2v['revature']
except KeyError:
    print("Word not in vocabulary")
```

#### Similarity Comparisons

```python
# Compare similarities between word pairs

pairs = [('cup', 'mug'), ('cup', 'bowl'), ('cup', 'beverage'), ('cup', 'cat')]
for w1, w2 in pairs:
    similarity = w2v.similarity(w1, w2)

print(f"Similarity between '{w1}' and '{w2}': {similarity:.2f}")
```

#### Finding Most Similar Words

```python
# Find words most similar to a given set

similar_words = w2v.most_similar(positive=['cup', 'mug'], topn=5)

print("Words most similar to ['cup', 'mug']:", similar_words)
```

#### Identifying Least Similar Words

```python
# Identify the least similar word in a set

odd_one_out = w2v.doesnt_match(['cup', 'cat', 'mug', 'jar'])

print("The odd one out:", odd_one_out)
```

---

## Advanced Tokenization Techniques

### Overview

Tokenization techniques such as stemming and lemmatizing are essential in natural language processing. They simplify text analysis and improve data handling efficiency.

### Stemming

- **Definition**: Reduces words to their root form, for instance, "learning" and "learner" to "learn".
- **Advantages**: Fast, focusing on core word meanings, beneficial where processing speed is critical.
- **Limitations**: Less precise than lemmatizing, can lead to understemming (e.g., "decided" becomes "decid") or overstemming (e.g., "university" and "universe" both become "univers").

#### Example: Using NLTK's Snowball Stemmer

```python
from nltk.stem.snowball import EnglishStemmer
from nltk.tokenize import word_tokenize

text = "The artist decided to create a new painting. Creating art is a form of self-expression. She hoped to create an atmosphere of creativity in her studio where she could freely create. The act of creation brought her joy, and she believed that anyone could create something beautiful with a bit of inspiration."

words = word_tokenize(text)
print(words)

# Output: ['The', 'artist', 'decided', 'to', 'create', 'a', 'new', 'painting', '.', 'Creating', 'art', 'is', 'a', 'form', 'of', 'self-expression', '.', 'She', 'hoped', 'to', 'create', 'an', 'atmosphere', 'of', 'creativity', 'in', 'her', 'studio', 'where', 'she', 'could', 'freely', 'create', '.', 'The', 'act', 'of', 'creation', 'brought', 'her', 'joy', ',', 'and', 'she', 'believed', 'that', 'anyone', 'could', 'create', 'something', 'beautiful', 'with', 'a', 'bit', 'of', 'inspiration']

stemmer = EnglishStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)

# Output: ['the', 'artist', 'decid', 'to', 'creat', 'a', 'new', 'paint', '.', 'creat', 'art', 'is', 'a', 'form', 'of', 'self-express', '.', 'she', 'hope', 'to', 'creat', 'an', 'atmospher', 'of', 'creativ', 'in', 'her', 'studio', 'where', 'she', 'could', 'freeli', 'creat', '.', 'the', 'act', 'of', 'creation', 'brought', 'her', 'joy', ',', 'and', 'she', 'believ', 'that', 'anyon', 'could', 'creat', 'someth', 'beauti', 'with', 'a', 'bit', 'of', 'inspir']
```

### Lemmatizing

- **Definition**: Finds the basic form of a word, more consistent than stemming.
- **Advantages**: Improves text analysis accuracy, reduces data size by limiting word variations.
- **Limitations**: Slower than stemming, may be ambiguous as it doesn't always consider word context.

#### Example: Using NLTK's WordNet Lemmatizer

```python
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()
string_for_lemmatizing = "Can you really have too many pens? They all serve different purposes and one simply cannot have too many!"
words = word_tokenize(string_for_lemmatizing)
print(words)

# Output: ['Can', 'you', 'really', 'have', 'too', 'many', 'pens', '?', 'They', 'all', 'serve', 'different', 'purposes', 'and', 'one', 'simply', 'can', 'not', 'have', 'too', 'many', '!']

lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print(lemmatized_words)

# Output: ['Can', 'you', 'really', 'have', 'too', 'many', 'pen', '?', 'They', 'all', 'serve', 'different', 'purpose', 'and', 'one', 'simply', 'can', 'not', 'have', 'too', 'many', '!']
```

---

## Part of Speech (POS) Tagging

### Overview

POS Tagging plays a pivotal role in natural language processing (NLP), identifying the grammatical role of each word in a sentence, such as nouns, verbs, adjectives, etc.

### Importance of POS Tagging

- **Context Understanding**: Helps models comprehend the context of words in a sentence, going beyond just recognizing the words and their frequency.
- **Applications in NLP**: Widely used in various NLP tasks like sentiment analysis, syntax analysis, speech recognition, and grammar style checking.
- **Foundation for Advanced NLP**: Serves as a key step before progressing to more complex tasks such as Named Entity Recognition (NER).

#### Key Note

- POS tagging is essentially a precursor to advanced NLP techniques like NER, setting the groundwork for deeper text analysis and processing.

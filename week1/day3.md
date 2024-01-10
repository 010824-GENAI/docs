# Week 1 - Day 3: Introduction to Python Word Embeddings

## Agenda

1. **Word2Vec:** Understanding the basics of Word2Vec for word embeddings.
2. **GloVe:** Learn about the Global Vectors for Word Representation (GloVe) model for word embeddings.
3. **Advanced Tokenization:** Deep dive into advanced techniques for tokenizing text data.
4. **POS Tagging:** Learn about Part-of-Speech (POS) tagging and its applications in NLP.
5. **Named Entity Recognition:** Understand the concept of Named Entity Recognition (NER) and how it's used in NLP.
6. **Text Similarity:** Explore different methods for calculating text similarity.
7. **Hands-on Session:** Practical exercises to apply the concepts learned.

## Learning Objectives

By the end of this session, you should be able to:

- Understand the basics of Word2Vec and GloVe for word embeddings.
- Understand advanced tokenization techniques.
- Understand the concept of POS tagging and Named Entity Recognition (NER).
- Understand different methods for calculating text similarity.
- Apply the learned concepts in practical exercises.

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

---

## Named Entity Recognition (NER)

### What is NER?

NER is the process of identifying and extracting named entities from text. These entities typically include nouns such as people's names, organizations, locations, dates, etc.

#### Example

In the sentence "Bill Gates and Paul Allen founded Microsoft", "Bill Gates" and "Paul Allen" are entities of type 'person', while "Microsoft" is an entity of type 'organization'.

### Applications of NER

- **Classifying Content**: Assists in scanning documents and categorizing them based on identified named entities.
- **Content Recommendation**: Enables suggestions for similar content with related entities.
- **PII Detection and Removal**: Useful in detecting and removing Personally Identifiable Information (PII) like names, phone numbers, or addresses from texts.

### Commonly Used Types of Named Entities

Refer to the NER diagram for a visual representation of different entity types.

![NER Diagram](../resources/ner-diagram.png)

### NER Example

NLTK offers a convenient ne_chunk function to detect Named Entities. Following is a code snippet that will walk you through the process of extracting NE and plotting the resulting tree.

```python
from nltk import ne_chunk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

ner_text = """
John Doe, a software engineer at ACME Corporation, recently attended a conference in New York City on January 15-17, 2023. The event, organized by Tech Innovations Inc., focused on artificial intelligence and machine learning. During the conference, John had the opportunity to network with professionals from Google, Microsoft, and other leading tech companies.
"""

tokens = word_tokenize(ner_text)
print(tokens)

pos_tagged = pos_tag(tokens)
print(pos_tagged)

tree = ne_chunk(pos_tagged)

tree.draw()
```

The function successfully identifies 'John Doe', 'ACME Corporation', 'New York City', 'Tech Innovations', 'Google', and 'Microsoft' as named entities.

---

## Text Similarity

### Introduction

Text similarity measures the likeness between two text pieces. It's important for search engines, recommending content, analyzing feelings, summarizing texts, and finding copied material.

### Cosine Similarity

- **What It Does**: Looks at the angle between two text vectors (word frequency lists).
- **How It's Used**: Good for comparing texts with lots of zeros in their word lists. However, it might miss the context or order of words.

### Euclidean Distance

- **What It Does**: Calculates the actual distance between two points (text vectors) in space.
- **NLP Use**: Helps figure out how different two document or sentence vectors are.

### Jaccard Similarity

- **What It Does**: Checks how much two sets overlap (like word sets in texts) by dividing their common words by their total words.
- **NLP Use**: Useful for grouping similar documents or finding duplicates. It cares about whether words are there, not how often they appear.

The following demonstrates calculating cosine similarity between two texts using sklearn

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample texts
text1 = "Natural language processing is fascinating."
text2 = "I'm intrigued by the wonders of natural language processing."

# Tokenize and vectorize the texts
vectorizer = CountVectorizer().fit_transform([text1, text2])

# Calculate cosine similarity
cosine_sim = cosine_similarity(vectorizer)

# Print the cosine similarity matrix
print(f"Cosine Similarity: {cosine_sim}")
```

The following is an sample implementation of Jaccard Similarity:

```python
# Function to calculate Jaccard similarity between two sets
def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

# Sample sets of words
set1 = {"natural", "language", "processing", "fascinating"}
set2 = {"intrigued", "by", "the", "wonders", "of", "natural", "language", "processing"}

# Calculate Jaccard similarity
jaccard_sim = jaccard_similarity(set1, set2)

# Print the Jaccard similarity
print(f"Jaccard Similarity: {jaccard_sim}")
```

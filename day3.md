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

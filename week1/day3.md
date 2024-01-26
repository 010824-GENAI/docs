# Day 3: More Tokenization, POS Tagging, NER, Word Embeddings, Text Similarity

## Agenda
- Stemming
- Lemmatization
- Part-of-Speech Tagging
- Named Entity Recognition
- Word Embeddings: Word2Vec
- Text Similarity

## Stemming
- text processing technique where we reduce words to their root form.
- focus on the core meaning of the word instead of being distracted by different ways in which they are being used. 
- words that they get reduced to may not be dictionary words.

## Lemmatization
- Coming from the word "lemma", lemmatizing is finding the lemma of a word. 
- Lemma in linguistics is the basic form of a word. 
- Ex: "be" would be the lemma for words like "is", "am", "are", "was", etc
- This technique yields more sophisticated and consistent result than stemming. 

## POS Tagging
- Part of Speech(POS) Tagging refers to a task that identifies each token with their part of speech. 
- Part of speech is a grammatical concept that denotes which role a word is playing in a sentence. The examples of them would be noun, verb, adverbs, adjectives, pronouns, etc. 
- enhances the understanding and analysis of textual data. Without POS tagging, we would be limited to the vocabularies and frequencies of appearance in the text.

## Named Entity Recognition
- Named entities are proper nouns that refer to specific entities. 
- Named entity recognition is the process of extracting Named Entities from the text.
- Closely related to POS tagging and Chunking

## Word Embeddings: Word2Vec, GloVe
- Humans are good with words. Computer is good with numbers
- Way to represent words as numbers

## Text Similarity
- How do we tell if a text is similar to another?
- Different matrics such as Euclidean distance, Cosine Similarity, Jaccard Similarity.
- Cosine Similarity: Compare the angle of 2 vectors
- Jaccard Similarity: Compare how many words they share

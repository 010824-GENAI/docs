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

## Hugging Face Transformers

### What are Hugging Face Transformers?

It's a library with pre-trained models for NLP tasks such as language translation, text generation, and sentiment analysis. Known for its user-friendliness, it's built on PyTorch and TensorFlow.

### Key Features

- **Ease of Use**: Designed for both beginners and experienced users.
- **Wide Range of Models**: Offers different model architectures for varied tasks like text classification and information extraction.
- **Flexibility**: Easy to switch between models and tasks, great for testing and fine-tuning.
- **Cost Efficiency**: Reduces computational costs.
- **Integration**: Compatible with popular deep learning frameworks.

### Installation Steps

1. **Transformers Library**: Install using pip with the command `pip install transformers`.
2. **Machine Learning Frameworks**:
   - For **PyTorch**: Use `pip install torch`.
   - For **TensorFlow**: Use `pip install tensorflow`.

### Quick Start Example

- **Using a Pre-trained Model**:
  - This example shows how to use a pipeline for sentiment analysis.
  - The code uses the `pipeline` function from the transformers package to classify a sample sentence.
  - The expected output for the sentence "Transformers library is amazing!" is a positive sentiment score.

Here's a simple example of using a pre-trained model:

```python
from transformers import pipeline

# Using a pipeline for sentiment analysis
classifier = pipeline('sentiment-analysis')

print(classifier('Transformers library is amazing!'))
# Expected Output: [{'label': 'POSITIVE', 'score': 0.9998774528503418}]
```

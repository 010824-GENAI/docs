# Project 2 (Due Wednesday 1/31/24)

For Project 2, we'll create a RAG application by extending your Project 1 with a vector database! You can continue working in your P1_your_name repository.
Same as before, on 1/31/24 at 3pm we will give an informal presentation of our projects. Please keep the demo to less than 4 minutes to keep things flowing. 

## Requirements
- Application should use persisted ChromaDB
- Application should use a text embedding model to create and retrieve embeddings
- Users should be able to load text or documents to ChromaDB
- The application should use text embedding model to retrieve appropriate documents for the user's question ("retrieval")
- The application should use an LLM to generate a response to the user's question based on the provided context ("generation")

## Stretch Goals
- Use different text file types (csv, markdown, pdf, etc)
- Validation on LLM Response
- Some interface of your choice (API, UI, etc.)
- Make LLM to remember your chat history
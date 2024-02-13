# LangChain +a

## Agenda
- Reminders
  - Labs
    - Test discovery or Env Var importing issues: Please restart the labs
    - for additional support, directly ping Valentina Kamalish (She's already in our meeting chat)
  - Project
    - Presentation 2/16 3PM
      - Our regular meeting link
  - [Week 5 Survey]( https://forms.office.com/r/WpzWUwSN9w), please and thank you
- LangChain +a

## LangChain +a
- technologies extending LangChain
  - LangSmith
  - LangGraph
  - LangServe
  - LangFlow
  - ...and more

### [LangSmith](https://docs.smith.langchain.com/)
- "LangSmith is a platform for building production-grade LLM applications." - LangChain team
- provides functionalities for you to debug, test, evaluate, and monitor chains and agents
  - works with LangChain and other LLM frameworks
- Currently in private beta, access via invitation only.
- [LangSmith Webinar 2/15/24 3PM](https://www.crowdcast.io/c/langsmith)

### [LangGraph](https://github.com/langchain-ai/langgraph)
- LangChain Expression Language(LCEL) supports sequential and branching execution (if/else)
- LangGraph allows for cycles
  - useful with newer, more advanced RAG architectures
    - [C-RAG](https://arxiv.org/pdf/2401.15884.pdf)
    - [self-RAG](https://arxiv.org/pdf/2310.11511.pdf)
    - [LangChain Cookbooks imprementing C-RAG and Self-RAG](https://github.com/langchain-ai/langgraph/tree/main/examples/rag)
- According to LangChain, anything that does not have cycles, should continue to use LCEL instead of LangGraph (ie. Directed Acyclical Graph (DAG))

### [LangServe](https://github.com/langchain-ai/langserve)
- API framework for LangChain Runnables and Chains
- uses FastAPI

### [LangFlow](https://docs.langflow.org/getting-started/creating-flows)
- GUI for LangChain (drag-and-drop)
- Useful for prototyping
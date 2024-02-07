from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceHubEmbeddings
import os
from dotenv import load_dotenv
from langchain_community.llms import HuggingFaceTextGenInference
from langchain_community.chat_models.huggingface import ChatHuggingFace
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
from langchain_core.runnables import RunnablePassthrough

from operator import itemgetter

load_dotenv()

hf_embeddings = HuggingFaceHubEmbeddings(model=os.getenv('EMBEDDING_URL'), huggingfacehub_api_token=os.getenv('HF_TOKEN'))

vdb = Chroma(persist_directory=os.getenv('CHROMA_PATH'), embedding_function=hf_embeddings)

# Retriever, also runnable
retriever = vdb.as_retriever()

chat_template = """
<|system|>
Answer the question only using the provided context
context: {context}
</s>
<|user|>
Question: {question} </s>
<|assistant|>
Answer:
"""

prompt = PromptTemplate.from_template(template=chat_template)

# This class is for LLM
llm = HuggingFaceTextGenInference(
    # This is Zephyr Model provided by Florida Blue
    inference_server_url="https://z8dvl7fzhxxcybd8.eu-west-1.aws.endpoints.huggingface.cloud",
    max_new_tokens=256,
    top_k=50,
    temperature=0.1,
    repetition_penalty=1.03,
    server_kwargs={
        "headers": {
            "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
            "Content-Type": "application/json",
        }
    }
)
chat_model = ChatHuggingFace(llm=llm)

# also called Pipelines
chain = ({
    "question": itemgetter("question"),
    "context": itemgetter("question") | retriever
} |
 prompt |
 chat_model |
 StrOutputParser())

# print(chain.invoke({"question": "What is norman door?"}))

# chain = RunnablePassthrough() | retriever

# print(chain.invoke("what is norman door?"))

# Using Chat Prompt Template
chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant chatbot. Answer user's question to the best of your ability Only using the context"),
    ("system", "Context: {context}"),
    ("human", "{question}"),
])

chain = ({
    "question": itemgetter("question"),
    "context": itemgetter("question") | retriever
} |
 chat_prompt_template | 
 chat_model |
 StrOutputParser())

# print(chain.invoke({"question": "What is norman door?"}))

memory = ConversationBufferMemory(return_messages=True, output_key="ai", input_key="human")

memory.save_context({"human": "What is Direct Manipulation?"}, {"ai": "Direct Manipulation refers to a type of human-computer interaction where users directly manipulate virtual objects on a screen to achieve their desired results, rather than using complex syntax or menus. It involves three key characteristics: a continuous representation of the object of interest, physical actions or labeled button presses instead of complex syntax, and rapid incremental reversible operations whose impact on the object of interest is immediately visible. The goal of Direct Manipulation is to provide users with a natural and intuitive way to interact with computers, making it easier to learn and use. However, the authors of the document you provided also acknowledge that more research is needed to fully understand the underlying basis for Direct Manipulation and why it feels so natural to users."})

chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant chatbot. Answer user's question to the best of your ability Only using the context and chat history"),
    ("system", "Context: {context}"),
    ("system", "Chat History: {chat_history}"),
    ("human", "{question}"),
])

chain = ({
    "question": itemgetter("question"),
    "context": itemgetter("question") | retriever,
    "chat_history": itemgetter("history")
} |
 chat_prompt_template | chat_model | StrOutputParser())

# print(chain.invoke({"question": "what is the topic of our conversation?", "history": memory.chat_memory.messages}))

template = PromptTemplate.from_template("<|system|>You are an summay assistant. Provided here is the conversation between the user and AI. What are they doing? Summarize the act of this conversation within 100 tokens to be used as memory for the AI to continue conversation with the user. History: {conversation_history}</s><|assistant|>Summary: ")

summary_chain = template | llm

# print(summary_chain.invoke({"conversation_history": memory.chat_memory.messages}))

print(chain.invoke({"question": "what are we talking about?", "history": summary_chain.invoke({"conversation_history": memory.chat_memory.messages})}))


# LCEL giving you a massive migraine? Use pre-made chains: https://python.langchain.com/docs/modules/chains 

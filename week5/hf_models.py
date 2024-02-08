import os 
from dotenv import load_dotenv
from langchain_community.llms import HuggingFaceTextGenInference
from langchain_community.chat_models.huggingface import ChatHuggingFace
from langchain_community.embeddings import HuggingFaceHubEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate, MessagesPlaceholder

load_dotenv()

llm = HuggingFaceTextGenInference(
    inference_server_url=os.getenv('HF_LLM'),
    max_new_tokens=256,
    top_k=50,
    temperature=0.01,
    repetition_penalty=1.03,
    server_kwargs={
        "headers": {
            "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
            "Content-Type": "application/json",
        }
    },
)

chat_model = ChatHuggingFace(llm=llm)

hf_embeddings = HuggingFaceHubEmbeddings(model=os.getenv('EMBEDDING_URL'), huggingfacehub_api_token=os.getenv('HF_TOKEN'))

vector_db = Chroma(persist_directory=os.getenv('CHROMA_PATH'), embedding_function=hf_embeddings)

retriever = vector_db.as_retriever(search_kwargs={"k": 1})
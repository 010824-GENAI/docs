from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceHubEmbeddings

from dotenv import load_dotenv
import os 

load_dotenv()

# HuggingFace Text Embedding Model
embeddings_model = HuggingFaceHubEmbeddings(model="https://c9ejquzh6yum3xqf.us-east-1.aws.endpoints.huggingface.cloud", huggingfacehub_api_token=os.getenv("HF_TOKEN"))

def batch_and_load(docs:list):
    batches = [docs[i:i + 31] for i in range(0, len(docs), 31)]
    for batch in batches:
        Chroma.from_documents(batch, embedding=embeddings_model, persist_directory=os.getenv("CHROMA_PATH"))

# Loading .txt file or raw text.
def process_raw_text(file_name, chunk_size=500, chunk_overlap=0):
    raw_text = TextLoader(file_name).load()
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(raw_text)
    batch_and_load(docs)

def process_pdf_files(file_path, chunk_size=500, chunk_overlap=0):
    from langchain_community.document_loaders import PyPDFLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    loader = PyPDFLoader(file_path=file_path)
    pages = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = text_splitter.split_documents(pages)
    batch_and_load(chunks)
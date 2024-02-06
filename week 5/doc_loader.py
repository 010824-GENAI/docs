from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceHubEmbeddings

from dotenv import load_dotenv
import os 

load_dotenv()

embeddings_model = HuggingFaceHubEmbeddings(model="https://c9ejquzh6yum3xqf.us-east-1.aws.endpoints.huggingface.cloud", huggingfacehub_api_token=os.getenv("HF_TOKEN"))

raw_text = TextLoader('./state_of_the_union.txt').load()
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)


docs = text_splitter.split_documents(raw_text)

batches = [docs[i:i + 31] for i in range(0, len(docs), 31)]

# for batch in batches:
Chroma.from_documents(docs, embedding=embeddings_model, persist_directory=os.getenv("CHROMA_PATH"))

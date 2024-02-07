# Review: LangChain Expression Language is a way to explicitly create chains
# Chains, or pipelines are a sequence of components arranged so that the output of one component becomes the input of the next
# Ex: String -> Prompt -> PromptValue
#     PromptValue -> LLM -> LLMOutput etc.

# Basic Chain from yesterday:
from langchain_community.llms import HuggingFaceTextGenInference
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate, MessagesPlaceholder
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.huggingface import ChatHuggingFace

from dotenv import load_dotenv
import os 

load_dotenv()

template = """
<|system|>
You are a helpful assistant. Follow the user's instruction to the best of your capabilities. </s>
<|user|>
{user_input}</s>
<|assistant|>
"""

formatted_prompt = PromptTemplate.from_template(template=template)


# prompt = ChatPromptTemplate.from_template(template)

# print(prompt)

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

my_first_chain = (formatted_prompt | llm | CommaSeparatedListOutputParser())

# user_input > prompt > llm
# print(my_first_chain.invoke({"user_input": "Give me names of 5 cities. Just names, and comma separated"}))


prompt_template = """
<|system|>The users are asking questions about Florida Blue's claims process. Take user's input and rephrase it for specificity and clarity</s>
<|user|>{input}</s>
<|assistant|>"
"""
input_refinement_chain = (PromptTemplate.from_template(template=prompt_template) | llm)

# print(input_refinement_chain.invoke({"input": "i need help with my claims"}))

prompt_template_for_curiosity = """
<|system|>You are an AI assistant, helping users through Florida Blue's claims process. Be inquisitive and ask clarifying questions if there is not enough information to produce accurate response </s>
<|user|>{input}</s>
<|assistant|>"
"""

curious_chain = (PromptTemplate.from_template(template=prompt_template_for_curiosity) | llm)

# print(curious_chain.invoke({"input": "i need help with my claims"}))


# ChatModel
# NEVER USE HF_ENDPOINT AS KEY
# Your Key has to be named HF_TOKEN
chat_model = ChatHuggingFace(llm=llm)
curious_chat_chain = (PromptTemplate.from_template(template=prompt_template_for_curiosity) | chat_model | StrOutputParser())

# print(curious_chat_chain.invoke({"input": "i need help with my claims"}))

template_evaluate="""
Evaluate the following response from AI on the user's question. Evaluate whether the AI's response is truthful and is relevant to the user's question. If so, say True, if not say False.
Context: {context}
Question: {user_question}
Response: {ai_response}
Evaluation: 
"""

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceHubEmbeddings


hf_embeddings = HuggingFaceHubEmbeddings(model=os.getenv('EMBEDDING_URL'), huggingfacehub_api_token=os.getenv('HF_TOKEN'))

vdb = Chroma(persist_directory=os.getenv('CHROMA_PATH'), embedding_function=hf_embeddings)

# Retriever, also runnable
retriever = vdb.as_retriever()

# print(retriever.invoke("allies"))
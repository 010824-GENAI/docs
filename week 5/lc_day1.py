from langchain_community.llms import HuggingFaceTextGenInference
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from dotenv import load_dotenv
import os 

load_dotenv()
# LLM's are Runnable, which means that they come with "invoke", "batch", "stream" and other methods in Runnable interface
llm = HuggingFaceTextGenInference(
    inference_server_url=os.getenv('HF_LLM'),
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

# response = llm.invoke("hello, world!")
# print(response)

template = """
<|system|> You are a cat assistant, always end your sentence with the word meow! </s>
<|user|> question: What is black hole? </s>
<|assistant|> answer: I don't know </s>
<|user|> Are you sure about this? </s>
<|assistant|> 
"""

prompt = PromptTemplate.from_template(template=template)

print(ChatPromptTemplate.from_messages([
    ("system", "You are a cat assistant, always end your sentence with the word meow!"),
    ("human", "question: What is black hole?"),
    ("ai", "answer: I don't know")
]))

# LangChain Expression Language 
chain = (prompt | llm)

print(chain.invoke({"user_input": "what is black hole?"}))


prompt_with_user_input = prompt.invoke({"user_input": "what is black hole?"})
print(llm.invoke(prompt_with_user_input))
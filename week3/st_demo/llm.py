import requests
import os
from dotenv import load_dotenv

load_dotenv()

def query_llm(prompt):

    api_url = os.getenv("LLM_URL")
    api_key = os.getenv("HUGGING_FACE_KEY")

    req_header = {
        "Authorization": f"Bearer {api_key}"
    }

    req_body = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens":100,
            "temperature": 1
        }
    }
    
    response = requests.post(api_url, json=req_body, headers=req_header)
    return response.json()
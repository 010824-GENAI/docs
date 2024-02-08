# Agents
# Previously, we used chains to interact with LLMs.
# In chains or pipelines, the workflow was hardcoded. LLM was simply part of the pipeline
# However, in Agents, LLM is being used as a reasoning agent.

# Agents are LLM with tools, which provides additional capabilitiese to the LLM.
# Tools are chains that are given to LLM with the instruction on when/how to use them.

from langchain.tools.retriever import create_retriever_tool
from hf_models import llm, chat_model, retriever
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.agents import AgentExecutor, create_json_chat_agent
from langchain_community.tools import DuckDuckGoSearchRun

retriever_tool = create_retriever_tool(
    retriever=retriever,
    name="search_human_computer_interaction_books",
    description="use this tool to look up anything that has to do with human computer interaction topic"
)

tools = [retriever_tool, DuckDuckGoSearchRun()]

prompt = hub.pull('hwchase17/react-chat-json')

print(prompt)
agent = create_json_chat_agent(chat_model, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

# agent_executor.invoke({"input":"what determines cat's coat color?"})
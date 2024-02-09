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
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

retriever_tool = create_retriever_tool(
    retriever=retriever,
    name="search_human_computer_interaction_books",
    description="use this tool to answer questions on human computer interaction topic"
)

tools = [retriever_tool, DuckDuckGoSearchRun()]

system = '''
You're an expert in Human computer interaction. You answer the user's question and converse with the user. You are inquisitive and ask follow up questions if the user's input doesn't have enough context. 
First, ask yourself if the user's input relates to the topics in human computer interaction.
If it is related to HCI use search_human_computer_interaction_books tool. 
For everything else, use duckduckgo_search tool or rely on your training data.
Always think if the question is related to human computer interaction topics before choosing a tool!

TOOLS
------
You can use tools to look up information that may be helpful in \
answering the users original question. The tools you can use are:

{tools}

RESPONSE FORMAT INSTRUCTIONS
----------------------------
When responding to human, Only use the following two options.
Option 1: When using a tool, please output a response like this:
```json
{{
    "action": string, \ The action to take. Must be one of {tool_names}
    "action_input": string \ The input to the action
}}
```
Option 2: For your final response, format response like this:
```json
{{
    "action": "Final Answer",
    "action_input": string \ your final answer
}}
```
'''

human = '''
Remember to respond with a markdown code snippet of a json blob with a single action, and NOTHING else.
Here is user's input: {input}
'''

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", human),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)

print(prompt)
agent = create_json_chat_agent(chat_model, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

from langchain_core.messages import AIMessage, HumanMessage

memory = [AIMessage(content="Hello! I'm an hci agent. How can I help you?")]
print("Hello! I'm an hci agent. How can I help you?")
while True:
    user_input = input()
    response = agent_executor.invoke({"input": user_input, "chat_history": memory})

    print(response['output'])
    memory.append(HumanMessage(content=user_input))
    memory.append(AIMessage(content=response['output']))
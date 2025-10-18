from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.chains import LLMMathChain
from langchain.agents import AgentExecutor, Tool
from langchain.agents.structured_chat.base import StructuredChatAgent

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# =============================================================================
# GENERATE PREDICTIONS
# =============================================================================

print("=" * 50)
print("1. GENERATE PREDICTIONS")
print("=" * 50)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    max_tokens=500,
)

response = llm.invoke("What are the 7 wonders of the world?")
print(f"Response: {response.content}")

# =============================================================================
# BETTER VERSION WITH HUMANMESSAGE AND SYSTEMMESSAGE
# =============================================================================

print("=" * 50)
print("2. BETTER VERSION WITH SYSTEM MESSAGE")
print("=" * 50)

chat_model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=500,
)

system_message = SystemMessage(
    content="You are a friendly pirate who loves to share knowledge. Always respond in pirate speech, use pirate slang, and include plenty of nautical references. Add relevant emojis throughout your responses to make them more engaging. Arr! ☠️🏴‍☠️"
)

question = "What are the 7 wonders of the world?"

messages = [
      system_message,
      HumanMessage(content=question)
]

response = chat_model.invoke(messages)

print("\nQuestion:", question)
print("\nPirate Response:")
print(response.content)

# =============================================================================
# PROMPT TEMPLATES
# =============================================================================

print("=" * 50)
print("3. PROMPT TEMPLATES")
print("=" * 50)

prompt_template = PromptTemplate.from_template(
    "List {n} cooking/meal titles for {cuisine} cuisine (name only)."
)

prompt = prompt_template.format(n=3, cuisine="italian")
response = llm.invoke(prompt)
print(f"Prompt Template Response: \n{response.content}")

# =============================================================================
# PROMPT TEMPLATES WITH PIPE OPERATOR
# =============================================================================

print("=" * 50)
print("4. PROMPT TEMPLATES WITH PIPE OPERATOR")
print("=" * 50)

prompt_template = PromptTemplate.from_template(
    "List {n} cooking/meal titles for {cuisine} cuisine (name only)."
)

chain = prompt_template | llm

response = chain.invoke({
    "n": 5,
    "cuisine": "Italian"
})

print("\nPrompt: List 5 cooking/meal titles for Italian cuisine (name only).")
print("\nResponse:")
print(response.content)

# =============================================================================
# GETTING STRUCTURED OUTPUT
# =============================================================================

print("=" * 50)
print("5. GETTING STRUCTURED OUTPUT")
print("=" * 50)

class Movie(BaseModel):
    title: str = Field(description="The title of the movie.")
    genre: list[str] = Field(description="The genre of the movie.")
    year: int = Field(description="The year the movie was released.")

parser = PydanticOutputParser(pydantic_object=Movie)

prompt_template_text = """
Response with a movie recommendation based on the query:\n
{format_instructions}\n
{query}
"""

format_instructions = parser.get_format_instructions()
prompt_template = PromptTemplate(
    template=prompt_template_text,
    input_variables=["query"],
    partial_variables={"format_instructions": format_instructions},
)

prompt = prompt_template.format(query="A 90s movie with Nicolas Cage.")
text_output = llm.invoke(prompt)
print(f"Raw output: {text_output.content}")

parsed_output = parser.parse(text_output.content)
print(f"Parsed output: {parsed_output}")

print("\n6. USING LCEL CHAIN")
chain = prompt_template | llm | parser
response = chain.invoke({"query": "A 90s movie with Nicolas Cage."})
print(f"LCEL response: {response}")

# =============================================================================
# BUILDING AN AI AGENT
# =============================================================================

print("=" * 50)
print("7. BUILDING AN AI AGENT")
print("=" * 50)

math_prompt = PromptTemplate.from_template(
    "Calculate the following expression and return the result in the format 'Answer: <number>': {question}"
)

llm_math_chain = LLMMathChain.from_llm(llm=llm, prompt=math_prompt, verbose=True)

search = DuckDuckGoSearchRun()

calculator = Tool(
    name="calculator",
    description="Use this tool for arithmetic calculations. Input should be a mathematical expression.",
    func=lambda x: llm_math_chain.invoke({"question": x}),
)

tools = [
    Tool(
        name="search",
        description="Search the internet for information about current events, data, or facts. Use this for looking up population numbers, statistics, or other factual information.",
        func=search.run
    ),
    calculator
]

agent = StructuredChatAgent.from_llm_and_tools(
    llm=llm,
    tools=tools
)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    handle_parsing_errors=True
)

print("\nRunning agent with query: 'What is the population difference between Tunisia and Algeria?'")
result = agent_executor.invoke({"input": "What is the population difference between TUN and ALG?"})
print(f"Agent result: {result['output']}")

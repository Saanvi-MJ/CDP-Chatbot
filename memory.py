from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def save_conversation(user_query, response):
    memory.save_context({"input": user_query}, {"output": response})

def load_conversation():
    history = memory.load_memory_variables({})
    return history.get("chat_history", [])  

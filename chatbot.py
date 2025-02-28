import os
import openai
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key is missing! Set it in a .env file or as an environment variable.")

openai.api_key = OPENAI_API_KEY


from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from retrieval import retrieve_relevant_docs
from memory import save_conversation, load_conversation

OPENAI_API_KEY = "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"

def chatbot_response(user_query):
    platform = next((p for p in ["segment", "mparticle", "lytics", "zeotap"] if p in user_query.lower()), None)
    
    if not platform:
        return "Please specify a platform (Segment, mParticle, Lytics, Zeotap)."
    relevant_docs = retrieve_relevant_docs(user_query, platform)
    doc_text = " ".join(relevant_docs)

    messages = load_conversation()
    messages.append(HumanMessage(content=f"User: {user_query}\nDocs: {doc_text}"))

 
    chat = ChatOpenAI(api_key=OPENAI_API_KEY)
    response = chat(messages)
    save_conversation(user_query, response.content)

    return response.content


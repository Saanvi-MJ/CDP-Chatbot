import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Error: OpenAI API key is missing! Set it in a .env file or as an environment variable.")

CDP_DOCS = {
    "segment": "https://segment.com/docs/",
    "mparticle": "https://docs.mparticle.com/",
    "lytics": "https://docs.lytics.com/",
    "zeotap": "https://docs.zeotap.com/home/en-us/"
}

def fetch_cdp_doc(platform):
    url = CDP_DOCS.get(platform.lower())
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    text_data = " ".join([p.text for p in soup.find_all("p")])

    if not text_data.strip():
        raise ValueError(f"Error: No content retrieved from {url}")

    return text_data

def create_vector_index(text_data):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = splitter.split_text(text_data)

    if not docs:
        raise ValueError("No valid text found for vector storage.")

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY).embed_documents(docs)

    if not embeddings:
        raise ValueError("Embeddings are empty. Check OpenAI API key and document content.")

    vectorstore = FAISS.from_texts(docs, OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY))
    return vectorstore

vector_stores = {}
for platform in CDP_DOCS.keys():
    try:
        print(f"Fetching data for {platform}...")
        text_data = fetch_cdp_doc(platform)
        vector_stores[platform] = create_vector_index(text_data)
        print(f"Vector store created for {platform}")
    except Exception as e:
        print(f"Error processing {platform}: {e}")

def retrieve_relevant_docs(query, platform):
    if platform.lower() not in vector_stores:
        return ["Error: No vector store found for the requested platform."]

    vectorstore = vector_stores.get(platform.lower())
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    query_vector = embeddings.embed_query(query)

    scores, indices = vectorstore.search(query_vector, k=3)
    return [vectorstore.index_to_doc[i] for i in indices]

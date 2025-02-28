# 🐵 CDP Support Chatbot  

A chatbot that provides answers to **"how-to"** questions related to Customer Data Platforms (**CDP**), including:  
- **Segment**  
- **mParticle**  
- **Lytics**  
- **Zeotap**  

This chatbot retrieves relevant information from official documentation and provides helpful responses.  

---

## Features  
**Supports OpenAI (GPT) and Google Gemini API**  
**Fetches data from CDP documentation**  
**Handles variations in questions**  
**Interactive web UI using Streamlit**  
**Uses FAISS or ChromaDB for vector search**  

---

## Installation  

### **Clone the Repository**  
```bash
git clone https://github.com/saanvi-mj/cdp-chatbot.git
cd cdp-chatbot
```

### Setup API Keys 

For OpenAI GPT

Get your OpenAI API Key from OpenAI
Create a .env file in your project folder and add:

OPENAI_API_KEY=your-openai-api-key-here

### Running the Chatbot

1️⃣ Start the Chatbot in the Terminal
python app.py

2️⃣ Run the Web UI (Streamlit)
streamlit run app.py

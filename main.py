import streamlit as st
from langchain_openai import OpenAI
from langchain import PromptTemplate
from langchain_groq import ChatGroq

st.set_page_config(
    page_title = "Blog Post Generator"
)

st.title("Blog Post Generator")

groq_api_key = st.sidebar.text_input(
    "Groq API Key",
    type = "password"
)

temperature = st.sidebar.number_input(
    "Temperatura",
    format="%.2f"
)

def generate_response(topic):
    llm = ChatGroq(model="llama3-70b-8192", api_key=groq_api_key, temperature=temperature)
    template = """
    As experienced startup and venture capital writer, 
    generate a 400-word blog post about {topic} in spanish.
    
    Your response should be in this format:
    First, print the blog post.
    Then, sum the total number of words on it and print the result like this: This post has X words.
    Remember, everything that you generate need to be in spanish.
    """
    prompt = PromptTemplate(
        input_variables = ["topic"],
        template = template
    )
    query = prompt.format(topic=topic)
    response = llm.invoke(query, max_tokens=2048)
    return st.write(response)


topic_text = st.text_input("Ingresa el Tema: ")
if not groq_api_key.startswith("gsk-"):
    st.warning("Enter Groq Key")
if groq_api_key.startswith("gsk-"):
    generate_response(topic_text)
        

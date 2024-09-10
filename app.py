import streamlit as st
import requests
from bs4 import BeautifulSoup
from langchain_ollama import OllamaLLM

# Initialize LLM for summarization
llm = OllamaLLM(model='llama3.1')

def search_topic(topic):
    search_url = f"https://www.google.com/search?q={topic}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.startswith('/url?q='):
            url = href.split('&')[0][7:]  # Clean URL
            links.append(url)
    return links[:5]  # Return top 5 links

def fetch_content(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all('p')
        content = ' '.join([para.get_text() for para in paragraphs])
        return content
    except Exception as e:
        st.write(f"Failed to fetch content from {url}: {e}")
        return ""

def summarize_content(contents):
    combined_text = " ".join(contents)
    # Pass the combined text as a list to match the expected input type
    result = llm.generate([f"Summarize the following content: {combined_text}"])
    
    # Check attributes to correctly extract the text from LLMResult
    if hasattr(result, 'generations'):
        # Access the first generation and extract the text
        summary = result.generations[0][0].text
    elif hasattr(result, 'text'):
        summary = result.text
    else:
        summary = "Summary not available."
    
    return summary

# Streamlit App
st.title("Information Summarizer")
st.write("Enter a topic, and this app will gather information, summarize it, and provide links to the sources.")

# User input
topic = st.text_input("Enter a topic:")

if st.button("Search and Summarize"):
    if topic:
        st.write(f"Searching for: {topic}")
        
        # Search for relevant links
        links = search_topic(topic)
        st.write("Found the following links:")
        for link in links:
            st.write(link)
        
        # Fetch content from links
        contents = [fetch_content(link) for link in links]
        
        # Summarize contents
        st.write("Generating summary...")
        summary = summarize_content(contents)
        
        # Display summary
        st.subheader("Summary of the Information Gathered:")
        st.write(summary)
        
        # Display sources
        st.subheader("Sources:")
        for link in links:
            st.write(link)
    else:
        st.write("Please enter a topic.")
